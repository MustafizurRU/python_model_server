from fastapi import FastAPI, File, HTTPException, Query
from fastapi.responses import FileResponse
from pydantic import BaseModel
import os
import subprocess

app = FastAPI()


class Prompt(BaseModel):
    prompt: str


@app.post("/input_prompts/")
async def input_prompts(prompt: Prompt):
    try:
        file_path = "input.txt"

        with open(file_path, "w") as file:
            file.write(prompt.prompt)

        return {"message": "Prompt saved successfully."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error saving prompt: {e}")


@app.get("/download_fbx/")
async def download_bvh(filename: str):
    bvh_folder = 'fbx_folder'  # Your folder containing BVH files
    filepath = os.path.join(bvh_folder, filename)

    if os.path.exists(filepath):
        return FileResponse(filepath, media_type='application/octet-stream', filename=filename)
    else:
        raise HTTPException(status_code=404, detail="File not found")


@app.get("/run_both/")
async def run_both(ext : str = Query(..., description="Path to config file"),
                   text_prompt: str = Query(..., description="Path to example file")):
    try:
        # Run demo.py command
        demo_command = f"python gen_t2m.py --gpu_id 0 --ext {ext} --text_prompt {text_prompt}"
        subprocess.run(demo_command, shell=True, check=True)

        # Run npy2fbx.py command with Blender
        blender_command = 'blender --background --python ./bvh2fbx/bvh2fbx.py'
        subprocess.run(blender_command, shell=True, check=True)

        return {"message": "All commands executed successfully."}

    except subprocess.CalledProcessError as e:
        # Handle any errors raised during command execution
        raise HTTPException(status_code=500, detail=f"Command execution failed: {e}")


if __name__ == "__main__":
    import uvicorn

    # Run the FastAPI application with uvicorn
    uvicorn.run(app, host="localhost", port=8000)
