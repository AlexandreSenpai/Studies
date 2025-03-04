from dataclasses import asdict
from src.app.core.interfaces.use_case import IUseCase
from src.app.use_cases.get_oauth_config import GetOauthConfigResponse, GetOauthConfigUseCase
from src.infra.adapters.repositories.oauth_repository import OauthRepository


class GetOauthConfigController:
    def __init__(self, get_oauth_config_use_case: IUseCase[None, GetOauthConfigResponse]):
        self.get_oauth_config_use_case = get_oauth_config_use_case

    async def perform(self):
        response = await self.get_oauth_config_use_case.execute()
        return asdict(response.data)
    
get_oauth_config_controller = GetOauthConfigController(
    get_oauth_config_use_case=GetOauthConfigUseCase(
        oauth_repository=OauthRepository()
    )
)