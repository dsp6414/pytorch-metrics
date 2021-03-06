# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 09:39:02 2020

@author: nsde
"""
import torch.nn.functional as F
from pytorch_metrics import ClassificationMetric


class FBeta(ClassificationMetric):
    name = 'fbeta'
    memory_efficient = True
    
    def __init__(self, beta, transform=None, is_multilabel=False):
        super().__init__(transform, is_multilabel)
        self.beta = beta

    def reset(self):
        self._tp = 0.0
        self._fp = 0.0
        self._fn = 0.0
        super().reset()

    def update(self, target, pred):
        self.check_input(target, pred)
        self.check_type(target, pred)
        target, pred = self.transform(target, pred)

        target = F.one_hot(target.long(), num_classes=self._num_classes)
        pred = F.one_hot(pred.long(), num_classes=self._num_classes)

        self._tp += (target * pred).sum(dim=-1).sum(dim=0)
        self._fn += (target * (1 - pred)).sum(dim=-1).sum(dim=0)
        self._fp += ((1 - target) * pred).sum(dim=-1).sum(dim=0)

    def compute(self):
        betasq1 = 1 + self.beta ** 2
        val = (betasq1 * self._tp) / (
            betasq1 * self._tp + self.beta ** 2 * self._fn + self._fp
        )
        try:
            return val.item()
        except:
            return val


class F1(FBeta):
    name = 'f1'
    memory_efficient = True
    
    def __init__(self, transform=None, is_multilabel=False):
        super().__init__(1.0, transform, is_multilabel)
