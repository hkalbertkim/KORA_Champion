# KORA Studio Demo Narration Script

## 1. Thirty-Second Opening

"KORA is not benchmarking H100 as a raw accelerator. KORA benchmarks when H100 should be used.

KORA Studio is a demo evidence surface for explaining execution-path selectivity. It shows a route decision across deterministic, cache, CPU, provider, GPU, and fallback paths, then connects that route to the committed benchmark evidence package."

## 2. Two-Minute Narration

"KORA is not benchmarking H100 as a raw accelerator. KORA benchmarks when H100 should be used.

This Studio view shows execution-path selectivity. A request is assigned to one of six execution paths: deterministic, cache, CPU, provider, GPU, or fallback. GPU is one path in the benchmark route space, not the default path for every request.

For this sample, Studio shows the selected path and the reason for that path. The route explanation is connected to the existing evidence package rather than to a production claim.

The dashboard evidence view shows the supporting chain. KORA has routing framework evidence, 100K routing selectivity evidence, bounded H100 routed subset measurement, multi-profile routing robustness evidence, 1M dry-run scale stability evidence, and bounded 1M H100 saturation subset evidence.

The claim-safe metric is compute-weighted GPU demand reduction in benchmark workloads. This demo does not claim production savings, customer workload savings, full provider/GPU live workload comparison, full 1M all-GPU measured execution, production representativeness, or official validation.

Studio explains the route decision. The dashboard shows the evidence chain behind it."

## 3. Five-Minute Narration

"KORA is not benchmarking H100 as a raw accelerator. KORA benchmarks when H100 should be used. In Korean: KORA의 실증 목표는 H100을 많이 쓰는 것이 아니라, H100을 써야 하는 요청과 쓰지 않아도 되는 요청을 구분하는 것이다.

This Studio demo starts with a route decision. The possible paths are deterministic, cache, CPU, provider, GPU, and fallback. KORA Studio is not presented as a broad production system. It is a demo evidence surface that makes execution-path selectivity visible.

The selected route is shown with an explanation. If the route is deterministic or cache, the viewer should understand that some benchmark requests do not require GPU execution. If the route is CPU, it stays in the local non-GPU path in the benchmark taxonomy. If the route is provider, the evidence boundary is bounded live provider evidence. If the route is GPU, the evidence connection is measured H100 runtime evidence, especially bounded H100 routed subset measurement. If the route is fallback, the route space is preserving a path for cases that should not be forced into an unsafe route.

Now the dashboard evidence view connects the Studio explanation to the committed evidence package. The routing framework report defines the benchmark path taxonomy. The 100K routing benchmark shows execution-path selectivity over a benchmark workload. The multi-profile report shows routing behavior across different benchmark distributions. The H100 routed subset report shows measured H100 execution for a bounded GPU-routed subset. The 1M scale and saturation report shows dry-run scale stability and bounded H100 saturation subset evidence.

The important wording is compute-weighted GPU demand reduction in benchmark workloads. That is a benchmark metric. It is not production savings, not customer workload savings, not full provider/GPU live workload comparison, and not full 1M all-GPU measured execution.

The final takeaway is simple: Studio explains the route decision, the dashboard packages the evidence chain, and the evidence supports execution-path selectivity claims within bounded benchmark workloads."

## 4. Korean Short Explanation

"KORA의 실증 목표는 H100을 많이 쓰는 것이 아니라, H100을 써야 하는 요청과 쓰지 않아도 되는 요청을 구분하는 것입니다. KORA Studio는 이 실행 경로 선택을 설명하는 데모 evidence surface입니다. 현재 증거는 benchmark workload에서의 compute-weighted GPU demand reduction과 bounded H100 routed subset measurement를 보여주며, production savings나 공식 검증을 주장하지 않습니다."

## 5. English Short Explanation

"KORA benchmarks when H100 should be used. KORA Studio explains execution-path selectivity by showing whether a request should use deterministic, cache, CPU, provider, GPU, or fallback execution. The evidence supports compute-weighted GPU demand reduction in benchmark workloads, not production savings."

## 6. Safe One-Liners

- "GPU is one execution path, not the default path for every request."
- "Studio explains the route decision; the dashboard shows the evidence chain."
- "The supported claim is compute-weighted GPU demand reduction in benchmark workloads."
- "The measured GPU evidence is bounded H100 routed subset measurement."
- "The 1M evidence is dry-run scale stability plus bounded saturation measurement."
- "This is execution-path selectivity evidence, not production savings evidence."
- "Measured, dry-run, and estimated evidence are kept separate."

## 7. Do-Not-Say List

Do not say:

- "KORA proves production cost reduction."
- "KORA proves customer workload savings."
- "KORA proves real infrastructure savings."
- "KORA proves 10x savings."
- "KORA completed a full provider/GPU live workload comparison."
- "KORA measured full 1M all-GPU execution."
- "KORA proves production representativeness."
- "KORA has a final paper-ready result."
- "KORA has formal government validation."
- "KORA has signed partner validation."
- "KORA proves broad workload superiority."
- "KORA proves energy reduction."

## 8. Evaluator Q&A

### Is this production cost savings?

No. The supported claim is compute-weighted GPU demand reduction in benchmark workloads. The evidence package does not claim production savings, customer workload savings, or real infrastructure savings.

### Is this full GPU benchmark proof?

No. KORA has measured H100 runtime evidence and bounded H100 routed subset measurement. It has not measured full 1M all-GPU execution and does not claim a full all-GPU workload proof.

### Is this only synthetic?

The current evidence is benchmark workload evidence. It includes dry-run routing benchmarks, bounded provider evidence, measured H100 runtime evidence, and bounded H100 routed subset measurement. It should not be described as production representativeness evidence.

### What does H100 evidence prove?

It proves that KORA has measured H100 runtime evidence for bounded benchmark settings, including routed subset measurement and bounded saturation subset measurement. It does not prove production H100 savings or full all-GPU execution.

### What does the dashboard prove?

The dashboard proves that the evidence chain is packaged in a static dashboard evidence view for reviewer inspection. It does not create new runtime evidence by itself.

### What does KORA Studio prove?

KORA Studio shows that execution-path selectivity can be explained as a demo evidence surface. It maps route decisions to existing benchmark evidence. It does not prove production deployment or broad workload superiority.

### What remains unproven?

The current package does not prove production savings, customer workload savings, real infrastructure savings, full provider/GPU live workload comparison, full 1M all-GPU measured execution, production representativeness, final paper readiness, official validation, signed partner validation, broad workload superiority, or energy reduction.
