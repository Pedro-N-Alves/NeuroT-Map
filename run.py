# %%
from pathlib import Path
import subprocess

# %%
workdir = Path("/home/zhenzong/analysis/NeuroT_Map")
scripts_dir = workdir / "NeuroT-Map"
lesion_dir = scripts_dir / "lesions"

# %%
# =================== 1. 找 lesion 文件 ===================
lesion_files = sorted(
    lesion_dir.glob(
        f"*.nii.gz"
    )
)
print("找到 lesion 文件数:", len(lesion_files))
if not lesion_files:
    raise RuntimeError("没有找到任何 lesion 文件，检查 lesion_dir ")

# %%
# =================== 3. 运行  ===================
lesion_names = [f.name.replace(".nii.gz", "") for f in lesion_files] #
print("将处理以下 lesion：")
for name in lesion_names:
    print(name)

cmd = ["python", "NeuroTmap.py", *lesion_names]

subprocess.run(cmd, cwd=scripts_dir, check=True)


