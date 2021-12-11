from abc import ABC, abstractmethod


class ProcessorBase(ABC):

    @abstractmethod
    def process(self, filepath):
        pass
