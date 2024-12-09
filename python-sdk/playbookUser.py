import json


class PlaybookUser:
    """
    This class is representing a Playbook user
    """

    def __init__(self,
                 user_id: str,
                 cognito_id: str,
                 tier_id: str,
                 email: str,
                 status: str,
                 user_type: str,
                 name: str,
                 has_active_subscription: bool,
                 gpu_usage_total: float,
                 gpu_usage_billing_period: float):
        self.user_id = user_id
        self.cognito_id = cognito_id
        self.tier_id = tier_id
        self.email = email
        self.status = status
        self.user_type = user_type
        self.name = name
        self.has_active_subscription = has_active_subscription
        self.gpu_usage_total = gpu_usage_total
        self.gpu_usage_billing_period = gpu_usage_billing_period

    @classmethod
    def from_json(cls, json_data: dict) -> "PlaybookUser":
        """
        Creates a PlaybookUser object from JSON data.
        :param json_data: JSON data to decode
        :return: A PlaybookUser object
        """
        return cls(
            user_id=json_data.get('id'),
            cognito_id=json_data.get('cognito_id'),
            tier_id=json_data.get('tier_id'),
            email=json_data.get('email'),
            status=json_data.get('status'),
            user_type=json_data.get('user_type'),
            name=json_data.get('name'),
            has_active_subscription=json_data.get('has_active_subscription'),
            gpu_usage_total=json_data.get('gpu_usage_total'),
            gpu_usage_billing_period=json_data.get('gpu_usage_billing_period'),
        )

    def to_json(self) -> str:
        return json.dumps({
            "id": self.user_id,
            "cognito_id": self.cognito_id,
            "tier_id": self.tier_id,
            "email": self.email,
            "status": self.status,
            "user_type": self.user_type,
            "name": self.name,
            "has_active_subscription": self.has_active_subscription,
            "gpu_usage_total": self.gpu_usage_total,
            "gpu_usage_billing_period": self.gpu_usage_billing_period,
        })
