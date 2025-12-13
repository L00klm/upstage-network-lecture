import logging
import logging.config
import os

LOGGING_CONFIG = {

}


def init_logging() -> None:
    """
    애플리케이션 시작 시 불러서 logging 전체 설정 적용
    """
    # logs 디렉토리 없으면 생성

    os.makedirs("logs", exist_ok=True)
    # 1) 로깅 기본 설정
    logging.basicConfig(
        format="%(asctime)s [%(levelname)s] %(filename)s:%(lineno)d - %(message)s",
        # format="%(asctime)s [%(levelname)s] %(message)s",
        level=logging.INFO,  # INFO 이상 레벨만 출력
        filename="logs/upstage-network-info.log"
    )
