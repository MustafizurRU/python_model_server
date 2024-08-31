# Project Name

## Overview

This project provides tools for processing and converting motion data. It includes a FastAPI server for handling API requests related to BVH files and their conversion, along with scripts for running and managing various processes.

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/yourusername/your-repo-name.git
   cd your-repo-name
   ```

2. **Create and Activate a Virtual Environment:**

   ```bash
   python -m venv env
   source env/bin/activate  # On Windows use `env\Scripts\activate`
   ```

3. **Install Dependencies:**

   ```bash
   pip install fastapi uvicorn
   ```

4. **Additional Requirements:**

   Ensure you have any additional libraries required by your scripts installed.

## Running the Server

1. **Start the FastAPI Server:**

   ```bash
   uvicorn main:app --reload
   ```

   The server will start on `http://localhost:8000`.

## API Endpoints

- **Download BVH File:**

  ```http
  http://localhost:8000/download_fbx/?filename=bvh_0_out.fbx
  ```

- **Run `joints2bvh.py`:**

  ```http
  http://localhost:8000/run_joints2bvh/
  ```

- **Run `demo.py`:**

  ```http
  http://localhost:8000/run_demo/?cfg=./config_AGPT.yaml&example=./input.txt
  ```

- **Run Both Commands:**

  ```http
  http://localhost:8000/run_both/?cfg=./config_AGPT.yaml&example=./input.txt
  ```

## Running the Scripts

1. **Run `demo.py` with Configuration:**

   ```bash
   python demo.py --cfg ./config_AGPT.yaml --example ./input.txt
   ```

2. **Run `joints2bvh.py`:**

   ```bash
   python ./npy2bvh/joints2bvh.py
   ```

## Contributing

1. Fork the repository
2. Create a new branch (`git checkout -b feature-branch`)
3. Make your changes
4. Commit your changes (`git commit -am 'Add new feature'`)
5. Push to the branch (`git push origin feature-branch`)
6. Create a new Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For any questions or issues, please contact [Your Name](mailto:your.email@example.com).
