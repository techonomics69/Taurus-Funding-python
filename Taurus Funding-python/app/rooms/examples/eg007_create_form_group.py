from docusign_rooms import FormGroupForCreate, FormGroupsApi
from flask import session, request

from app.rooms import create_rooms_api_client


class Eg007CreateFormGroupController:
    @staticmethod
    def get_args():
        """Get required session and request arguments"""
        return {
            "account_id": session["ds_account_id"],     # Represents your {ACCOUNT_ID}
            "access_token": session["ds_access_token"],  # Represents your {ACCESS_TOKEN}
            "form_group_name": request.form.get("form_group_name"),
        }

    @staticmethod
    def worker(args):
        """
        1. Create an API client with headers
        2. Create FormGroupForCreate object
        3. POST the form using SDK
        """

        # Step 2 start

        # Create an API with headers
        api_client = create_rooms_api_client(access_token=args["access_token"])

        # Step 2 end

        # Step 3 start

        # Create FormGroupForCreate object
        form = FormGroupForCreate(name=args["form_group_name"])

        # Step 3 end

        # Step 4 start

        # Post the form object using SDK
        form_groups_api = FormGroupsApi(api_client)
        response = form_groups_api.create_form_group(
            body=form, account_id=args["account_id"]
        )

        # Step 4 end

        return response
