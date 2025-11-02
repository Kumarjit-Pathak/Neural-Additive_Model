"""
Model utilities
Agent 2: Model Architect
"""
import os
os.environ['KERAS_BACKEND'] = 'jax'

import keras
import joblib
from pathlib import Path
from loguru import logger


def save_model(model, filepath: str, save_format='keras'):
    """
    Save Keras model

    Args:
        model: Keras model
        filepath: Path to save model
        save_format: 'keras' or 'h5'
    """
    filepath = Path(filepath)
    filepath.parent.mkdir(parents=True, exist_ok=True)

    logger.info(f"Saving model to {filepath}")
    model.save(filepath, save_format=save_format)
    logger.info("Model saved successfully")


def load_model(filepath: str, custom_objects=None):
    """
    Load Keras model

    Args:
        filepath: Path to model file
        custom_objects: Dict of custom objects

    Returns:
        Loaded model
    """
    from .constrained_layers import MonotonicPositiveLayer, MonotonicNegativeLayer, BetaGammaLayer
    from .hierarchical_nam import HierarchicalNAM

    default_custom_objects = {
        'MonotonicPositiveLayer': MonotonicPositiveLayer,
        'MonotonicNegativeLayer': MonotonicNegativeLayer,
        'BetaGammaLayer': BetaGammaLayer,
        'HierarchicalNAM': HierarchicalNAM
    }

    if custom_objects:
        default_custom_objects.update(custom_objects)

    logger.info(f"Loading model from {filepath}")
    model = keras.models.load_model(filepath, custom_objects=default_custom_objects)
    logger.info("Model loaded successfully")

    return model


def save_scalers(scalers: dict, filepath: str):
    """Save sklearn scalers"""
    filepath = Path(filepath)
    filepath.parent.mkdir(parents=True, exist_ok=True)

    logger.info(f"Saving scalers to {filepath}")
    joblib.dump(scalers, filepath)


def load_scalers(filepath: str) -> dict:
    """Load sklearn scalers"""
    logger.info(f"Loading scalers from {filepath}")
    return joblib.load(filepath)
