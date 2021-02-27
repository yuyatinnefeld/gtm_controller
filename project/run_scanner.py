from decouple import config
from service import get_service
from gtm_scanner import GTMScanner
from pprint import pprint

CLIENT_SECRETS = config("CLIENT_SECRETS")
ACCOUNT_ID = config("ACCOUNT_ID")
CONTAINER_NAME = config("CONTAINER_NAME")
CONTAINER_ID = config("CONTAINER_ID")
WORKSPACE_NAME = config("WORKSPACE_NAME")
WORKSPACE_ID = config("WORKSPACE_ID")

scope = ["https://www.googleapis.com/auth/tagmanager.edit.containers"]
service = get_service("tagmanager", "v2", scope, CLIENT_SECRETS)

gtm_scanner = GTMScanner(service)


def display_all_accounts():
    accounts = gtm_scanner.get_accounts()
    gtm_scanner.print_account_list(accounts)


def display_account(account):
    gtm_scanner.print_account(account)


def display_all_containers(account_id):
    containers = gtm_scanner.get_containers(account_id)
    gtm_scanner.print_container_list(containers)


def display_container(container):
    gtm_scanner.print_container(container)


def display_all_workspaces(account_id, container_id):
    workspaces = gtm_scanner.get_workspaces(account_id, container_id)
    gtm_scanner.print_workspace_list(workspaces)


def display_workspace(workspace):
    gtm_scanner.print_workspace(workspace)


def display_gtm_overview():
    accounts = gtm_scanner.get_accounts()
    gtm_scanner.print_total_info(accounts)


if __name__ == "__main__":

    ### CALL ACCOUNT INFO ###
    # display_all_accounts()
    # account = gtm_scanner.get_account(ACCOUNT_ID)
    # display_account(account)

    ### CALL CONTAINER INFO ###
    # display_all_containers(ACCOUNT_ID)
    # containers = gtm_scanner.get_containers(ACCOUNT_ID)
    # container = gtm_scanner.get_container(containers, CONTAINER_NAME)
    # display_container(container)

    ### CALL WORKSPACE INFO ###
    # display_all_workspaces(ACCOUNT_ID, CONTAINER_ID)
    workspaces = gtm_scanner.get_workspaces(ACCOUNT_ID, CONTAINER_ID)
    workspace = gtm_scanner.get_workspace(workspaces, WORKSPACE_NAME)
    # display_workspace(workspace)

    ### CALL GTM OVERVIEW ###
    # display_gtm_overview()

    ### SELECT TAG & TRIGGER & VARIABLE ###
    workspace_path = workspace.get_path()
    tag = gtm_scanner.get_tag_by_name(workspace_path, 'GA_PV_TAG')
    trigger = gtm_scanner.get_trigger_by_name(workspace_path, 'PV_TRIGGER')
    variable = gtm_scanner.get_variable_by_name(workspace_path, 'COOKIE_SAMPLE')

    ### SHOW TAG & TRIGGER & VARIABLE INFO ###
    gtm_scanner.print_tag_info(tag)
    gtm_scanner.print_trigger_info(trigger)
    gtm_scanner.print_variable_info(variable)