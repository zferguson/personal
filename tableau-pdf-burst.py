import tableauserverclient as TSC
import os

# === CONFIGURATION ===
TABLEAU_SERVER = "https://your-tableau-server.com"
SITE_ID = ""  # Leave blank for default site
PROJECT_NAME = "Your Project"
WORKBOOK_NAME = "Your Workbook"
VIEW_NAME = "Your View"  # This is the dashboard or sheet name
FILTER_FIELD = "Region"  # Change to your actual filter field
FILTER_VALUES = ["East", "West", "Central", "South"]  # List of values to burst
OUTPUT_DIR = "pdf_bursts"

# === AUTHENTICATION ===
auth = TSC.PersonalAccessTokenAuth(
    token_name="your-token-name",
    personal_access_token="your-token-value",
    site_id=SITE_ID
)

# === SCRIPT START ===
with TSC.Server(TABLEAU_SERVER, auth) as server:
    server.use_server_version()

    # Create output directory if not exists
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # Find the workbook
    all_workbooks, _ = server.workbooks.get()
    workbook = next((wb for wb in all_workbooks if wb.name == WORKBOOK_NAME), None)
    if not workbook:
        raise Exception(f"Workbook '{WORKBOOK_NAME}' not found")

    # Get views from the workbook
    server.workbooks.populate_views(workbook)
    view = next((v for v in workbook.views if v.name == VIEW_NAME), None)
    if not view:
        raise Exception(f"View '{VIEW_NAME}' not found in workbook '{WORKBOOK_NAME}'")

    # Iterate over each filter value and download PDF
    for value in FILTER_VALUES:
        pdf_req_option = TSC.PDFRequestOptions()
        pdf_req_option.vf(FILTER_FIELD, value)

        output_filename = os.path.join(OUTPUT_DIR, f"{VIEW_NAME}_{value}.pdf")
        print(f"Generating PDF for {FILTER_FIELD} = {value}...")

        server.views.populate_pdf(view, pdf_req_option)
        with open(output_filename, "wb") as f:
            f.write(view.pdf)

        print(f"Saved: {output_filename}")