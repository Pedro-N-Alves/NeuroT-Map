# %%
from pathlib import Path
import subprocess
import math
import sys
import pandas as pd
from concurrent.futures import ThreadPoolExecutor, as_completed

# %%
workdir = Path("/home/linzhenzong/NeuroT_map/")
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
# =================== 2. 筛选掉空lesion ===================
volumn_file = workdir/ "lesion_volumes.csv"
df = pd.read_csv(volumn_file)
df["ID"] = df["ID"].astype(str).str.strip()
df["voxels"] = pd.to_numeric(df["voxels"],errors="coerce")
zero_ids = set(df.loc[df["voxels"] == 0, "ID"])
filtered_lesion_files = []
skipped = []
for f in lesion_files:
    lesion_id = f.name.split("_")[0]
    if lesion_id in zero_ids:
        skipped.append(f.name)
        continue
    filtered_lesion_files.append(f)
lesion_files = filtered_lesion_files
print(f"病灶为0跳过的文件数为：" , len(skipped))
print(f"待分析的文件数为：" , len(lesion_files))


# =================== 3. 运行  ===================
lesion_names = [f.name.replace(".nii.gz", "") for f in lesion_files] #

batch_size = 100
max_workers = 50  

#for i in range(0, len(lesion_names),batch_size):
#    batch = lesion_names[i : i+batch_size]
#    cmd = [sys.executable, "NeuroTmap.py", *batch]
#    subprocess.run(cmd, cwd=scripts_dir, check=True)

def run_one_batch(batch):
    cmd = [sys.executable, "NeuroTmap.py", *batch]
    subprocess.run(cmd, cwd=scripts_dir, check=True)
    return len(batch)

batches = [
    lesion_names[i:i + batch_size]
    for i in range(0, len(lesion_names), batch_size)
]

print(f"总批次数: {len(batches)}")
print(f"并行进程数: {max_workers}")

done = 0
with ThreadPoolExecutor(max_workers=max_workers) as executor:
    futures = {executor.submit(run_one_batch, batch): batch for batch in batches}

    for future in as_completed(futures):
        batch = futures[future]
        try:
            n = future.result()
            done += 1
            print(f"完成批次 {done}/{len(batches)}，本批 {n} 个 lesion")
        except Exception as e:
            print(f"批次失败，前3个 lesion: {batch[:3]}")
            raise e
   
print("全部完成")


