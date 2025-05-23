"""
This type stub file was generated by pyright.
"""

from abc import ABC
from typing import List

class BaseDoc(ABC):
    """Classe base para todas as classes referentes a documentos."""

    def validate(self, doc: str = ...) -> bool:
        """Método para validar o documento desejado."""
        ...

    def validate_list(self, docs: List[str]) -> List[bool]:
        """Método para validar uma lista de documentos desejado."""
        ...

    def generate(self, mask: bool = ...) -> str:
        """Método para gerar um documento válido."""
        ...

    def generate_list(
        self, n: int = ..., mask: bool = ..., repeat: bool = ...
    ) -> List[str]:
        """Gerar uma lista do mesmo documento."""
        ...

    def mask(self, doc: str = ...) -> str:
        """Mascara o documento enviado"""
        ...
