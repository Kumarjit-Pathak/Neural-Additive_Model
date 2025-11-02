# Agent 2: Model Architect - Task List

## Phase 1: Keras 3 Setup & Architecture Design (Week 1-2)
- [ ] Install and configure Keras 3 with JAX backend
- [ ] Verify Keras 3 installation and backend
- [ ] Design constrained layer interfaces
- [ ] Create layer design documentation

## Phase 2: Constrained Layers Implementation (Week 2)
- [ ] Implement MonotonicPositiveLayer (Keras Layer subclass)
- [ ] Implement MonotonicNegativeLayer (Keras Layer subclass)
- [ ] Implement BetaGammaLayer (parametric investment function)
- [ ] Implement HillLayer (alternative investment function)
- [ ] Test each layer independently

## Phase 3: Hierarchical NAM Structure (Week 2-3)
- [ ] Design HierarchicalNAM (Keras Model subclass)
- [ ] Implement brand-level feature networks
- [ ] Implement SKU-level feature networks
- [ ] Implement hierarchical combination logic
- [ ] Implement get_feature_contribution() method
- [ ] Test forward pass and gradient flow

## Phase 4: Baseline Models (Week 3)
- [ ] Implement Linear Regression baseline
- [ ] Implement Ridge Regression baseline
- [ ] Implement simple Neural Network baseline
- [ ] Create model factory pattern

## Phase 5: Model Utilities (Week 3)
- [ ] Model serialization (save/load .keras files)
- [ ] Model summary and visualization
- [ ] Weight initialization strategies
- [ ] Create model architecture documentation

## Deliverables
- `src/models/constrained_layers.py`
- `src/models/hierarchical_nam.py`
- `src/models/baseline_models.py`
- `src/models/model_utils.py`
- `docs/model_architecture.md`
