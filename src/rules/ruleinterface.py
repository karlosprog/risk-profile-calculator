from abc import ABC, abstractmethod

from src.model.riskprofile import RiskProfile


# Simulating an interface
class RuleInterface(ABC):

    @abstractmethod
    def apply(self, risk_profile: RiskProfile):
        pass
