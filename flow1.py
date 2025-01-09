import random
from prefect import flow, task


@task(log_prints=True)
def auto_classify_ai():
    print("Auto classification Started")
    classified_to_str = ["pdf","excel","none"]
    classified_to = random.choice(classified_to_str)
    if classified_to == "pdf":
        response = pdf_classify()
    elif classified_to == "excel":
        response = excel_classify()
    else:
        response = "none"
    return f"return from auto classification {response}"

@task(log_prints=True)
def excel_classify():
    print("Excel classification Started")
    return "return form excel classify"

@task(log_prints=True)
def pdf_classify():
    print("Pdf classification Started")
    return "return form pdf classify"

@task(log_prints=True)
def upload_files(upload_type):
    print("uplaod file")
    if upload_type == "auto_classify_ai":
        response_ai = auto_classify_ai()
        print(response_ai)
    elif upload_type == "excel":
        response_excel = excel_classify()
        print(response_excel)
    elif upload_type == "pdf":
        response_pdf = pdf_classify()
        print(response_pdf)
    return "complete"


@flow(log_prints=True)
def flow1(upload_type):
    upload_files(upload_type)
    return "flow1"


# if __name__ == "__main__":
#     flow1.from_source(
#         source="https://github.com/sushilkhadka165/prefect-testing.git",
#         entrypoint="/mnt/veracrypt1/d_tests/prefect_test/flow1.py:flow1"
#     ).deploy(
#         name="upload-service",
#         work_pool_name="upload_flow",
#     )