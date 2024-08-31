pip install fastapi
pip install uvicorn


python demo.py --cfg ./config_AGPT.yaml --example ./input.txt
python ./npy2bvh/joints2bvh.py

For Api Calling:
Download BVH file: 
http://localhost:8000/download_fbx/?filename=bvh_0_out.fbx
Run joints2bvh.py: 
http://localhost:8000/run_joints2bvh/
Run demo.py: http://localhost:8000/run_demo/?cfg=./config_AGPT.yaml&example=./input.txt
Run Both Commands: http://localhost:8000/run_both/?cfg=./config_AGPT.yaml&example=./input.txt
