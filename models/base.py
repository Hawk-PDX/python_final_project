from sqlalchemy import Column, Integer, DateTime, func
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class BaseModel(Base):
    __abstract__ = True

    # Common attributes
    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, default=func.now(), nullable=False)
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now(), nullable=False)

    # Utility methods
    def save(self, session):
        """Save the current instance to the database."""
        session.add(self)
        session.commit()

    def delete(self, session):
        """Delete the current instance from the database."""
        session.delete(self)
        session.commit()

    def update(self, session, **kwargs):
        """Update the current instance with new values."""
        for key, value in kwargs.items():
            setattr(self, key, value)
        session.commit()
        session.refresh(self)  # Refresh the instance

    def __repr__(self):
        return f"<{self.__class__.__name__} id={self.id}>"