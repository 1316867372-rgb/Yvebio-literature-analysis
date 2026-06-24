# -*- coding: utf-8 -*-
"""生成研究流程图。
默认使用环境变量 INFOGRAPHIC_TOOL_DIR 指向的本地工作流工具；
如未设置则跳过，由SKILL.md中的步骤5提示用户手动处理。
"""

import os, sys, io


def generate(prompt_file):
    tool_dir = os.environ.get("INFOGRAPHIC_TOOL_DIR", "")
    if not tool_dir or not os.path.isdir(tool_dir):
        print(
            "[SKIP] INFOGRAPHIC_TOOL_DIR not configured. Skipping infographic generation."
        )
        print("       Set env var: INFOGRAPHIC_TOOL_DIR=<path_to_infographic_tool>")
        return

    sys.path.insert(0, tool_dir)
    os.chdir(tool_dir)
    from generate_infographic import process_infographic_task

    out_dir = os.path.dirname(prompt_file)
    tmp = os.path.join(out_dir, "_info_tmp")
    os.makedirs(tmp, exist_ok=True)

    success = process_infographic_task(
        md_file_path=prompt_file,
        task_dir=tmp,
        size="4:3",
        image_count=1,
        image_model="gpt-image2",
    )

    if success:
        import shutil

        for f in os.listdir(tmp):
            src = os.path.join(tmp, f)
            if f.lower().endswith(".png"):
                base = os.path.splitext(os.path.basename(prompt_file))[0]
                dst = os.path.join(
                    out_dir, base.replace("_AI绘图提示词", "_研究流程") + ".png"
                )
                shutil.move(src, dst)
                print(f"[OK] {dst}  ({os.path.getsize(dst):,} bytes)")
        shutil.rmtree(tmp, ignore_errors=True)
    else:
        print("[FAILED] Infographic generation failed.")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python generate_infographic.py <prompt_txt_path>")
        sys.exit(1)
    generate(sys.argv[1])
