using System.Globalization;
using System.Text;
using System.Text.Json;

namespace VerityFlow.Runtime;

internal sealed record Summary(
    string Title,
    string Grade,
    double HealthScore,
    double Coverage,
    double MeanSupport,
    double MeanDiversity,
