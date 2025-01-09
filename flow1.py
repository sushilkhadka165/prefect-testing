import random
import time
from prefect import flow, task


@task(log_prints=True)
def auto_classify_ai():
    print("Auto classification Started")
    classified_to_str = ["pdf","excel","none"]
    classified_to = random.choice(classified_to_str)
    time.sleep(4)
    return (f"return from auto classification {classified_to}", classified_to)

@task(log_prints=True)
def excel_classify():
    print("Excel classification Started")
    return "return form excel classify"

@task(log_prints=True)
def pdf_classify():
    print("Pdf classification Started")
    return "return form pdf classify"

@task(log_prints=True)
def upload_files():
    print("uplaod file")
    time.sleep(3)
    return "file uploaded"


@flow(log_prints=True)
def flow1(upload_type):
    response_upload = upload_files.submit()
    if upload_type == "auto_classify_ai":
        response_ai = auto_classify_ai.submit()
        response_aix, classified_to = response_ai.result()
        print(response_aix)
        upload_type = classified_to

    if upload_type == "excel":
        response_excel = excel_classify()
        print(response_excel)
    elif upload_type == "pdf":
        response_pdf = pdf_classify()
        print(response_pdf)
    return "flow1"


# if __name__ == "__main__":
#     flow1.from_source(
#         source="https://github.com/sushilkhadka165/prefect-testing.git",
#         entrypoint="flow1.py:flow1"
#     ).deploy(
#         name="upload-service",
#         work_pool_name="upload_flow_managed",
#     )