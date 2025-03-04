from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Optional, TypedDict, cast
from uuid import uuid4

class PropsWithDefaults(TypedDict):
    id: str | int
    created_at: Optional[datetime]
    updated_at: Optional[datetime]

class Entity[T]:
    def __init__(self,
                 id: Optional[str],
                 created_at: Optional[datetime],
                 updated_at: Optional[datetime]) -> None:
        
        self.id = id or str(uuid4())
        self.created_at = created_at or datetime.now(tz=timezone.utc)
        self.updated_at = updated_at or datetime.now(tz=timezone.utc)

    def __repr__(self) -> str:
        non_special_attrs = [f"{chave}={valor!r}" for chave, valor in self.__dict__.items() if not isinstance(valor, list) and not isinstance(valor, dict)]
        special_attrs = [f"{chave}={valor!r}" for chave, valor in self.__dict__.items() if isinstance(valor, list) or isinstance(valor, dict)]
        return f"{self.__class__.__name__}({', '.join([*non_special_attrs, *special_attrs])})"
    
    def to_dict(self) -> T:
        """Converts the entity to a dictionary.

        Returns:
            A dictionary representation of the entity.
        """
        data = self.__dict__ 
        for key in data:
            instances = [isinstance(data[key], _type) for _type in [str, int, bool, 
                                                                    float, dict, list, 
                                                                    set]]
            if any(instances) is False:
                data[key] = str(data[key])
                
        return cast(T, data)