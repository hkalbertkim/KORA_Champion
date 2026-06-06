# KORA Studio Demo Script

## 1. Opening Message

KORA is not benchmarking H100 as a raw accelerator. KORA benchmarks when H100 should be used.

KORA Studio is the demo evidence surface for explaining execution-path selectivity. It shows how a request can be routed across deterministic, cache, CPU, provider, GPU, and fallback paths, then connects that decision to the existing KORA Core evidence chain.

## 2. What the Screen Shows

The demo should show:

| Screen area | Viewer should see |
| --- | --- |
| Route decision | The selected execution path for the sample request |
| Path explanation | Why the route is appropriate under benchmark routing rules |
| Evidence mapping | Which report or evidence file supports the path |
| Dashboard bridge | A link or transition to the dashboard evidence view |
| Claim boundary | A visible reminder that the package is benchmark evidence |

The screen should be capture-ready. Avoid small text, hidden evidence links, or panels that require unstated context.

## 3. Demo Sequence

1. Start on the Studio route decision view.
2. State the core message.
3. Show one sample request and the selected route.
4. Explain why that route is not automatically GPU.
5. Walk through deterministic, cache, CPU, provider, GPU, and fallback path meanings.
6. Open the evidence mapping panel.
7. Connect the Studio view to the static dashboard evidence view.
8. Show the 100K routing selectivity result.
9. Show the bounded H100 routed subset measurement.
10. Show the 1M scale and bounded saturation evidence.
11. End on claim boundaries and non-claims.

## 4. Expected Viewer Interpretation

The viewer should conclude:

- KORA has a route-aware benchmark and evidence package.
- Studio helps explain the routing decision surface.
- Execution-path selectivity is the benchmark target.
- H100 is used when the route calls for GPU execution.
- Existing evidence supports benchmark workload claims.
- The package does not claim production savings or official validation.

## 5. Explaining Routing Decisions

Use this explanation:

KORA evaluates request characteristics and assigns an execution path. The path can be deterministic, cache, CPU, provider, GPU, or fallback. The benchmark asks whether the route is acceptable under the oracle-labeled workload and whether unsafe misroutes are avoided. The resulting route distribution is used to measure execution-path selectivity.

For GPU-routed requests, KORA connects the route to measured H100 evidence through bounded H100 routed subset measurement and bounded H100 saturation subset evidence. For non-GPU paths, the point is not that GPU is slow. The point is that H100 should not be treated as the default path for every request.

## 6. Path Explanation Guide

| Path | Demo explanation | Evidence connection |
| --- | --- | --- |
| Deterministic | The request can be handled by deterministic logic in the benchmark route space | Routing benchmark framework |
| Cache | The request is cache-eligible and should not consume GPU execution in the benchmark | 100K, multi-profile, and 1M route distribution |
| CPU | The request fits a CPU execution path in the benchmark taxonomy | Routing benchmark framework |
| Provider | The request is routed to provider execution where appropriate | Bounded live provider evidence |
| GPU | The request requires local GPU execution in the benchmark route space | H100 routed subset and saturation subset evidence |
| Fallback | The request is sent to fallback when forcing another route would be unsafe | Route correctness and unsafe misroute metrics |

## 7. Connecting Dashboard Evidence to Studio

Use Studio for the decision explanation, then use the dashboard evidence view for the evidence chain.

Recommended transition:

"Studio shows the route decision. The dashboard shows the evidence package behind that decision: 100K execution-path selectivity, measured H100 routed subset execution, multi-profile robustness, and 1M scale with bounded saturation measurement."

Show:

- Core message.
- KPI cards.
- Evidence chain timeline.
- 100K routing selectivity table.
- H100 measured execution table.
- Multi-profile robustness table.
- 1M scale and saturation table.
- Claim boundary section.

## 8. What Not To Say

Do not say:

- KORA proves production cost reduction.
- KORA proves customer workload savings.
- KORA proves real infrastructure savings.
- KORA proves 10x savings.
- KORA completed a full provider/GPU live workload comparison.
- KORA measured full 1M all-GPU execution.
- KORA proves production representativeness.
- KORA has a final paper-ready result.
- KORA has formal government validation.
- KORA has signed partner validation.
- KORA proves broad workload superiority.
- KORA proves energy reduction.

## 9. Short 2-Minute Script

"KORA is not benchmarking H100 as a raw accelerator. KORA benchmarks when H100 should be used.

This Studio view shows execution-path selectivity. A request is assigned to one of six paths: deterministic, cache, CPU, provider, GPU, or fallback. The important point is that GPU is one path, not the default path.

For this sample, Studio shows the selected route and the reason for that route. The route explanation is connected to the benchmark evidence package rather than to a production claim.

The dashboard evidence view shows the supporting chain. KORA has 100K dry-run routing selectivity evidence, bounded H100 routed subset measurement, multi-profile routing robustness evidence, 1M dry-run scale stability evidence, and bounded 1M H100 saturation subset evidence.

The safe claim is that KORA can show compute-weighted GPU demand reduction in benchmark workloads. This is not a production savings claim, not a full provider/GPU live workload comparison, and not full 1M all-GPU measured execution.

Studio is therefore the explanation surface. KORA Core is the benchmark evidence chain behind it."

## 10. Longer 5-Minute Script

"KORA is not benchmarking H100 as a raw accelerator. KORA benchmarks when H100 should be used. In Korean: KORA의 실증 목표는 H100을 많이 쓰는 것이 아니라, H100을 써야 하는 요청과 쓰지 않아도 되는 요청을 구분하는 것이다.

This Studio demo is designed to make that idea visible. The screen starts with a request and a route decision. The possible paths are deterministic, cache, CPU, provider, GPU, and fallback. KORA Studio does not present GPU as the automatic answer. It shows the execution path selected for the request and explains why that path is appropriate under the benchmark routing rules.

For deterministic and cache paths, the viewer should understand that some benchmark requests do not require GPU execution. For CPU, the request fits a local non-GPU path in the benchmark taxonomy. For provider, KORA has bounded live provider evidence, so the claim stays limited to provider path readiness. For GPU, KORA connects the route to measured H100 runtime evidence through bounded H100 routed subset measurement and bounded 1M H100 saturation subset evidence. For fallback, the route space keeps an explicit path for requests that should not be forced into an unsafe route.

Now we move from Studio to the dashboard evidence view. The dashboard packages the committed evidence chain. The 100K benchmark shows execution-path selectivity across the route space. The multi-profile benchmark shows that the routing framework can be evaluated across different benchmark distributions. The 1M benchmark shows dry-run scale stability, and the saturation subset shows bounded measured H100 execution. The dashboard also keeps measured, dry-run, and estimated evidence separated.

The key claim is compute-weighted GPU demand reduction in benchmark workloads. That wording matters. This is not a claim about production cost reduction, customer workload savings, real infrastructure savings, full 1M all-GPU measured execution, or official validation.

The reviewer takeaway is that KORA Studio explains the route decision, while KORA Core provides the benchmark evidence chain. Together they show execution-path selectivity in a public-safe July 31 evidence package."

## 11. Demo Close

End with:

"KORA Studio is the explanation surface. The evidence chain remains KORA Core benchmark evidence, bounded measured H100 evidence, and the static dashboard evidence view."
