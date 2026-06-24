# -*- coding: utf-8 -*-
"""从PDF提取每张Fig为独立PNG。支持 Fig./FIGURE 格式。输出到PDF同目录，命名：{basename} Fig.{n}.png"""

import fitz, os, re, sys, io
from PIL import Image
from io import BytesIO


def extract(pdf_path):
    doc = fitz.open(pdf_path)
    out_dir = os.path.dirname(pdf_path)
    basename = os.path.splitext(os.path.basename(pdf_path))[0]

    extracted = []
    for i, page in enumerate(doc):
        text = page.get_text()
        # 匹配 "Fig. 1", "Fig 1", "FIGURE 1", "Figure 1"
        fig_matches = re.findall(r"(?:Fig\.?\s*|FIGURE\s+)(\d+)", text, re.IGNORECASE)
        images = page.get_images(full=True)
        if fig_matches and images:
            for match in fig_matches:
                fig_num = int(match)
                if not any(e["num"] == fig_num for e in extracted):
                    extracted.append({"num": fig_num, "page": i + 1, "img_idx": 0})

    extracted.sort(key=lambda x: x["num"])

    for item in extracted:
        page = doc[item["page"] - 1]
        images = page.get_images(full=True)
        if item["img_idx"] >= len(images):
            continue
        xref = images[item["img_idx"]][0]
        base = doc.extract_image(xref)
        img = Image.open(BytesIO(base["image"]))
        out_name = f"{basename} Fig.{item['num']}.png"
        out_path = os.path.join(out_dir, out_name)
        img.save(out_path, "PNG")
        print(f"  [OK] {out_name}  ({img.width}x{img.height})")

    doc.close()
    return len(extracted)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python extract_figures.py <pdf_path>")
        sys.exit(1)
    n = extract(sys.argv[1])
    print(f"\nDone. {n} figures extracted.")
