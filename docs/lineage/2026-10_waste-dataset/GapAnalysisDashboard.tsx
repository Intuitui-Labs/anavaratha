import { useState } from 'react';
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '@/components/ui/card';
import { Badge } from '@/components/ui/badge';
import { Button } from '@/components/ui/button';
import { AlertTriangle, TrendingDown } from 'lucide-react';

const phases = [
  {
    phase: 'Collection',
    coverage: 'Moderate',
    infrastructure: 'Partial',
    geographic: 'Uneven',
    funding: 'Limited',
    severity: 'High',
    gaps: 'Limited rural coverage, informal sector not integrated, no standardized systems',
  },
  {
    phase: 'Segregation at Source',
    coverage: 'Low',
    infrastructure: 'Minimal',
    geographic: 'Very Limited',
    funding: 'Minimal',
    severity: 'Critical',
    gaps: 'No mandatory segregation, limited awareness, no enforcement mechanisms',
  },
  {
    phase: 'Transportation',
    coverage: 'Moderate',
    infrastructure: 'Partial',
    geographic: 'Uneven',
    funding: 'Limited',
    severity: 'High',
    gaps: 'Limited fleet, inefficient routing, no real-time tracking',
  },
  {
    phase: 'Transfer Stations',
    coverage: 'Low',
    infrastructure: 'Minimal',
    geographic: 'Very Limited',
    funding: 'Minimal',
    severity: 'Critical',
    gaps: 'Only 1-2 functional stations, no standardized design, no intermediate processing',
  },
  {
    phase: 'Treatment & Processing',
    coverage: 'Low',
    infrastructure: 'Minimal',
    geographic: 'Very Limited',
    funding: 'Limited',
    severity: 'Critical',
    gaps: 'Limited composting, minimal recycling, no hazardous waste processing',
  },
  {
    phase: 'Waste-to-Energy',
    coverage: 'Low',
    infrastructure: 'Minimal',
    geographic: 'Very Limited',
    funding: 'Limited',
    severity: 'High',
    gaps: 'Only 1 facility, limited capacity, high capital costs',
  },
  {
    phase: 'Recycling',
    coverage: 'Low',
    infrastructure: 'Partial',
    geographic: 'Uneven',
    funding: 'Limited',
    severity: 'High',
    gaps: 'Informal sector dominates, only 3-4 MRFs, no material standards',
  },
  {
    phase: 'Composting & Organic Waste',
    coverage: 'Very Low',
    infrastructure: 'Minimal',
    geographic: 'Very Limited',
    funding: 'Minimal',
    severity: 'Critical',
    gaps: 'No segregation, <1% composted, no community infrastructure',
  },
  {
    phase: 'E-Waste Management',
    coverage: 'Moderate',
    infrastructure: 'Partial',
    geographic: 'Limited',
    funding: 'Limited',
    severity: 'High',
    gaps: 'Only 3-4 facilities, limited collection, export-dependent',
  },
  {
    phase: 'Hazardous Waste',
    coverage: 'Low',
    infrastructure: 'Minimal',
    geographic: 'Very Limited',
    funding: 'Limited',
    severity: 'Critical',
    gaps: 'Only 2 facilities, no comprehensive inventory, poor enforcement',
  },
  {
    phase: 'Landfill Management',
    coverage: 'Moderate',
    infrastructure: 'Partial',
    geographic: 'Limited',
    funding: 'Limited',
    severity: 'High',
    gaps: 'Aging landfills, no engineered facilities, poor environmental controls',
  },
  {
    phase: 'Monitoring & Compliance',
    coverage: 'Low',
    infrastructure: 'Minimal',
    geographic: 'Very Limited',
    funding: 'Limited',
    severity: 'High',
    gaps: 'No real-time monitoring, weak enforcement, no digital tracking',
  },
  {
    phase: 'Awareness & Education',
    coverage: 'Low',
    infrastructure: 'Minimal',
    geographic: 'Very Limited',
    funding: 'Minimal',
    severity: 'Critical',
    gaps: 'Low public awareness, limited school programs, no behavioral change',
  },
  {
    phase: 'Financing',
    coverage: 'Low',
    infrastructure: 'Minimal',
    geographic: 'Very Limited',
    funding: 'Critical',
    severity: 'Critical',
    gaps: 'Heavy donor dependence, limited domestic funding, no sustainable models',
  },
  {
    phase: 'Research & Development',
    coverage: 'Low',
    infrastructure: 'Minimal',
    geographic: 'Very Limited',
    funding: 'Limited',
    severity: 'High',
    gaps: 'Limited research centers, few innovation initiatives, brain drain',
  },
];

const getSeverityColor = (severity: string) => {
  switch (severity) {
    case 'Critical':
      return 'bg-red-100 text-red-800 border-red-300';
    case 'High':
      return 'bg-amber-100 text-amber-800 border-amber-300';
    case 'Moderate':
      return 'bg-yellow-100 text-yellow-800 border-yellow-300';
    default:
      return 'bg-slate-100 text-slate-800 border-slate-300';
  }
};

const getCoverageColor = (coverage: string) => {
  switch (coverage) {
    case 'Very Low':
      return 'bg-red-50 text-red-700';
    case 'Low':
      return 'bg-orange-50 text-orange-700';
    case 'Moderate':
      return 'bg-amber-50 text-amber-700';
    case 'High':
      return 'bg-green-50 text-green-700';
    default:
      return 'bg-slate-50 text-slate-700';
  }
};

export default function GapAnalysisDashboard() {
  const [selectedPhase, setSelectedPhase] = useState<string | null>(null);
  const [severityFilter, setSeverityFilter] = useState<string | null>(null);

  const filteredPhases = severityFilter
    ? phases.filter((p) => p.severity === severityFilter)
    : phases;

  const selectedPhaseData = selectedPhase
    ? phases.find((p) => p.phase === selectedPhase)
    : null;

  const criticalCount = phases.filter((p) => p.severity === 'Critical').length;
  const highCount = phases.filter((p) => p.severity === 'High').length;

  return (
    <div className="space-y-6">
      {/* Summary Cards */}
      <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
        <Card className="bg-gradient-to-br from-red-50 to-orange-50 border-red-200">
          <CardContent className="pt-6">
            <div className="flex items-center justify-between">
              <div>
                <p className="text-sm text-red-700 font-medium">Critical Gaps</p>
                <p className="text-3xl font-bold text-red-800">{criticalCount}</p>
              </div>
              <AlertTriangle className="w-8 h-8 text-red-600 opacity-20" />
            </div>
          </CardContent>
        </Card>

        <Card className="bg-gradient-to-br from-amber-50 to-yellow-50 border-amber-200">
          <CardContent className="pt-6">
            <div className="flex items-center justify-between">
              <div>
                <p className="text-sm text-amber-700 font-medium">High Priority</p>
                <p className="text-3xl font-bold text-amber-800">{highCount}</p>
              </div>
              <TrendingDown className="w-8 h-8 text-amber-600 opacity-20" />
            </div>
          </CardContent>
        </Card>

        <Card className="bg-gradient-to-br from-slate-50 to-slate-100 border-slate-200">
          <CardContent className="pt-6">
            <div className="flex items-center justify-between">
              <div>
                <p className="text-sm text-slate-700 font-medium">Total Phases</p>
                <p className="text-3xl font-bold text-slate-800">{phases.length}</p>
              </div>
              <div className="w-8 h-8 bg-slate-300 opacity-20 rounded" />
            </div>
          </CardContent>
        </Card>
      </div>

      {/* Filters */}
      <Card>
        <CardHeader>
          <CardTitle>Waste Lifecycle Gap Analysis</CardTitle>
          <CardDescription>
            Comprehensive assessment of gaps across 15 waste management lifecycle phases
          </CardDescription>
        </CardHeader>
        <CardContent className="space-y-4">
          <div className="flex gap-2 flex-wrap">
            <Button
              variant={severityFilter === null ? 'default' : 'outline'}
              size="sm"
              onClick={() => setSeverityFilter(null)}
            >
              All Phases
            </Button>
            <Button
              variant={severityFilter === 'Critical' ? 'default' : 'outline'}
              size="sm"
              onClick={() => setSeverityFilter('Critical')}
            >
              Critical Only
            </Button>
            <Button
              variant={severityFilter === 'High' ? 'default' : 'outline'}
              size="sm"
              onClick={() => setSeverityFilter('High')}
            >
              High Priority
            </Button>
          </div>
        </CardContent>
      </Card>

      {/* Phases Grid */}
      <div className="grid grid-cols-1 lg:grid-cols-2 gap-4">
        {/* Phase List */}
        <div className="space-y-2">
          {filteredPhases.map((phase) => (
            <Card
              key={phase.phase}
              className={`cursor-pointer transition-all ${
                selectedPhase === phase.phase
                  ? 'ring-2 ring-teal-500 bg-teal-50'
                  : 'hover:shadow-md'
              }`}
              onClick={() => setSelectedPhase(phase.phase)}
            >
              <CardContent className="pt-4 pb-4">
                <div className="flex items-start justify-between gap-3">
                  <div className="flex-1">
                    <h4 className="font-semibold text-slate-900 mb-2">{phase.phase}</h4>
                    <div className="flex gap-2 flex-wrap">
                      <Badge variant="outline" className={getCoverageColor(phase.coverage)}>
                        {phase.coverage}
                      </Badge>
                      <Badge
                        variant="outline"
                        className={getSeverityColor(phase.severity)}
                      >
                        {phase.severity}
                      </Badge>
                    </div>
                  </div>
                </div>
              </CardContent>
            </Card>
          ))}
        </div>

        {/* Phase Details */}
        <div>
          {selectedPhaseData ? (
            <Card className="sticky top-4">
              <CardHeader>
                <CardTitle className="text-lg">{selectedPhaseData.phase}</CardTitle>
                <CardDescription>Detailed gap analysis</CardDescription>
              </CardHeader>
              <CardContent className="space-y-4">
                <div className="grid grid-cols-2 gap-4">
                  <div className="bg-slate-50 p-3 rounded-lg">
                    <p className="text-xs text-slate-600 mb-1">Current Coverage</p>
                    <p className="font-semibold text-slate-900">{selectedPhaseData.coverage}</p>
                  </div>
                  <div className="bg-slate-50 p-3 rounded-lg">
                    <p className="text-xs text-slate-600 mb-1">Infrastructure</p>
                    <p className="font-semibold text-slate-900">
                      {selectedPhaseData.infrastructure}
                    </p>
                  </div>
                  <div className="bg-slate-50 p-3 rounded-lg">
                    <p className="text-xs text-slate-600 mb-1">Geographic Coverage</p>
                    <p className="font-semibold text-slate-900">
                      {selectedPhaseData.geographic}
                    </p>
                  </div>
                  <div className="bg-slate-50 p-3 rounded-lg">
                    <p className="text-xs text-slate-600 mb-1">Funding Status</p>
                    <p className="font-semibold text-slate-900">{selectedPhaseData.funding}</p>
                  </div>
                </div>

                <div className="border-t pt-4">
                  <p className="text-sm font-semibold text-slate-900 mb-2">Key Gaps</p>
                  <p className="text-sm text-slate-700">{selectedPhaseData.gaps}</p>
                </div>

                <div className={`p-3 rounded-lg ${getSeverityColor(selectedPhaseData.severity)}`}>
                  <p className="text-xs font-semibold mb-1">Gap Severity</p>
                  <p className="font-bold">{selectedPhaseData.severity}</p>
                </div>
              </CardContent>
            </Card>
          ) : (
            <Card className="sticky top-4">
              <CardContent className="pt-6 text-center text-slate-600">
                <p>Select a lifecycle phase to view detailed gap analysis</p>
              </CardContent>
            </Card>
          )}
        </div>
      </div>
    </div>
  );
}
