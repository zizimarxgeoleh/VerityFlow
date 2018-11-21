using System.Text.Json;

namespace VerityFlow.Runtime;

internal sealed record ClaimEntry(
    string ClaimId,
    string ClaimText,
    string Topic,
    string Verdict,
