# Agent 3: Training Specialist - Task List

## Phase 1: Training Infrastructure (Week 2-3)
- [ ] Implement NAMTrainer class with Keras
- [ ] Custom loss function (NAMLoss - Keras Loss subclass)
- [ ] Constraint loss computation
- [ ] Hierarchical regularization loss
- [ ] Smoothness regularization loss
- [ ] Keras callbacks (EarlyStopping, ModelCheckpoint, ReduceLR)
- [ ] MLflow integration for experiment tracking

## Phase 2: Training Execution (Week 3)
- [ ] Train baseline models (Linear, Ridge, NN)
- [ ] Train NAM model with standard Keras fit()
- [ ] Implement custom training loop (if needed)
- [ ] Monitor constraint violations during training
- [ ] Log metrics to MLflow

## Phase 3: Walk-Forward Validation (Week 3-4)
- [ ] Implement WalkForwardSplitter (time-series aware)
- [ ] Implement WalkForwardNAMTrainer
- [ ] Execute walk-forward validation (6 folds)
- [ ] Collect OOS predictions and metrics
- [ ] Analyze fold-to-fold stability
- [ ] Generate WFO validation report

## Phase 4: Hyperparameter Tuning (Week 4-5)
- [ ] Set up Optuna study
- [ ] Define hyperparameter search space
- [ ] Execute hyperparameter optimization
- [ ] Select best hyperparameters
- [ ] Retrain with optimal hyperparameters

## Phase 5: Alternative Optimization (Optional - Week 5)
- [ ] Implement coordinate descent trainer
- [ ] Implement block coordinate descent
- [ ] Compare optimization strategies

## Deliverables
- `src/training/trainer.py`
- `src/training/loss_functions.py`
- `src/training/callbacks.py`
- `src/training/walk_forward.py`
- `src/training/hyperparameter_tuning.py`
- Trained models in outputs/models/
- MLflow experiments
