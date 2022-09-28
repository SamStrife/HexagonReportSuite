import tempfile
from pprint import pprint

from dotenv import load_dotenv
import os

from office365.runtime.auth.user_credential import UserCredential
from office365.sharepoint.client_context import ClientContext


load_dotenv()
sharepoint_site_url = "https://hexagonleasing.sharepoint.com/sites/ReportSuite/"
sharepoint_username = os.getenv("SHAREPOINTASSETFILEUSER")
sharepoint_password = os.getenv("SHAREPOINTASSETFILEPASSWORD")
sharepoint_file_path = os.getenv("SHAREPOINTASSETMASTERFILEFILEURL")


def master_file_backup():
    ctx = ClientContext(sharepoint_site_url).with_credentials(UserCredential(sharepoint_username,sharepoint_password))

    folder_rel_url = "/sites/ReportSuite/Reports/Asset File/Master Sheet/Asset File Master.xlsx"
    folder = ctx.web.get_folder_by_server_relative_url(folder_rel_url).select("Exists").get().execute_query()
    if folder.exists:
        print("Folder is found")
    else:
        print("Folder not found")
