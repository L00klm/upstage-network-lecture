from fastapi.params import Depends
import chromadb

from app.core.db import get_chroma_client
from sqlalchemy.orm import Session

from app.core.db import get_db
from app.repository.user_repo import UserRepository
from app.repository.vector_repo import VectorRepository, ChromaDBRepository
from app.service.user_service import UserService
from app.service.vector_service import VectorService
from app.service.embedding_service import EmbeddingService
from app.service.agent_service import AgentService

def get_user_repository(db: Session = Depends(get_db)) -> UserRepository:
    return UserRepository(db)

def get_vector_repository(chroma_client: chromadb.HttpClient = Depends(get_chroma_client)) -> VectorRepository:
    return ChromaDBRepository(chroma_client)


def get_embedding_service() -> EmbeddingService:
    return EmbeddingService()


def get_vector_service(
    vector_repo: VectorRepository = Depends(get_vector_repository),
    embedding_service: EmbeddingService = Depends(get_embedding_service)
) -> VectorService:
    return VectorService(vector_repository=vector_repo, embedding_service=embedding_service)


def get_user_service(user_repo: UserRepository = Depends(get_user_repository)) -> UserService:
    return UserService(user_repo=user_repo)


def get_agent_service(vector_service: VectorService = Depends(get_vector_service)) -> AgentService:
    return AgentService(vector_service=vector_service)
