import { useState } from 'react';
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '@/components/ui/card';
import { Badge } from '@/components/ui/badge';
import { Button } from '@/components/ui/button';
import { ChevronDown, ChevronUp } from 'lucide-react';

const timelineEvents = [
  {
    year: 1994,
    event: 'Proposal for waste disposal infrastructure development',
    category: 'Planning',
    significance: 'high',
    description: 'Initial planning phase for structured waste management infrastructure',
  },
  {
    year: 1999,
    event: 'Western Province Waste Management Statute enacted',
    category: 'Legislation',
    significance: 'high',
    description: 'Legal framework established for waste management in Western Province',
  },
  {
    year: 2005,
    event: 'Waste Management Authority of Western Province established',
    category: 'Governance',
    significance: 'high',
    description: 'Creation of dedicated authority to oversee waste management operations',
  },
  {
    year: 2006,
    event: 'Landfill gas emission studies conducted',
    category: 'Research',
    significance: 'medium',
    description: 'Scientific assessment of Karadiyana and Budgamuwa dumpsites',
  },
  {
    year: 2010,
    event: 'Increased waste generation from post-war development',
    category: 'Infrastructure',
    significance: 'medium',
    description: 'Rapid urbanization and development led to waste volume increases',
  },
  {
    year: 2013,
    event: 'Significant increase in waste management research',
    category: 'Research',
    significance: 'medium',
    description: 'Academic and professional research on waste management challenges',
  },
  {
    year: 2015,
    event: 'Success Environmental Engineering Solutions established',
    category: 'Private Sector',
    significance: 'low',
    description: 'Private company enters waste management sector',
  },
  {
    year: 2019,
    event: 'Lanka Environment Fund established; Infinity Green International founded',
    category: 'Private Sector',
    significance: 'medium',
    description: 'Conservation fund and e-waste company launched',
  },
  {
    year: 2021,
    event: 'Kerawalapitiya waste-to-energy facility becomes operational',
    category: 'Infrastructure',
    significance: 'high',
    description: "Sri Lanka's first waste-to-energy plant begins operations",
  },
  {
    year: 2022,
    event: 'Veolia completes merger with Suez',
    category: 'Global Markets',
    significance: 'medium',
    description: 'Major global consolidation in waste management industry',
  },
  {
    year: 2024,
    event: 'Sri Lanka waste-to-energy plant recognized globally',
    category: 'Infrastructure',
    significance: 'high',
    description: 'International recognition of waste-to-energy achievements',
  },
  {
    year: 2024,
    event: 'UNDP-Coca-Cola Plastics Circularity Project begins',
    category: 'International Initiative',
    significance: 'high',
    description: 'USD 1.1M project for plastic waste management in Colombo District',
  },
  {
    year: 2025,
    event: 'Kattankudy recycling centre opens',
    category: 'Infrastructure',
    significance: 'medium',
    description: 'First solid waste recycling centre under Clean Sri Lanka Programme',
  },
  {
    year: 2025,
    event: 'EU grants €8 million for biodiversity and waste',
    category: 'International Funding',
    significance: 'high',
    description: 'European Union support for environmental initiatives',
  },
  {
    year: 2027,
    event: 'UNDP-Coca-Cola project completion target',
    category: 'International Initiative',
    significance: 'medium',
    description: 'Expected completion of plastic waste management framework',
  },
];

const getCategoryColor = (category: string) => {
  switch (category) {
    case 'Planning':
      return 'bg-blue-100 text-blue-800';
    case 'Legislation':
      return 'bg-purple-100 text-purple-800';
    case 'Governance':
      return 'bg-indigo-100 text-indigo-800';
    case 'Research':
      return 'bg-cyan-100 text-cyan-800';
    case 'Infrastructure':
      return 'bg-teal-100 text-teal-800';
    case 'Private Sector':
      return 'bg-green-100 text-green-800';
    case 'Global Markets':
      return 'bg-amber-100 text-amber-800';
    case 'International Initiative':
      return 'bg-pink-100 text-pink-800';
    case 'International Funding':
      return 'bg-rose-100 text-rose-800';
    default:
      return 'bg-slate-100 text-slate-800';
  }
};

const getSigColor = (sig: string) => {
  switch (sig) {
    case 'high':
      return 'border-l-4 border-l-red-500';
    case 'medium':
      return 'border-l-4 border-l-amber-500';
    default:
      return 'border-l-4 border-l-slate-300';
  }
};

export default function TimelineExplorer() {
  const [expandedYear, setExpandedYear] = useState<number | null>(null);
  const [categoryFilter, setCategoryFilter] = useState<string | null>(null);

  const filteredEvents = categoryFilter
    ? timelineEvents.filter((e) => e.category === categoryFilter)
    : timelineEvents;

  const categories = Array.from(new Set(timelineEvents.map((e) => e.category)));

  return (
    <div className="space-y-6">
      <Card>
        <CardHeader>
          <CardTitle>Waste Management Timeline (1994-2027)</CardTitle>
          <CardDescription>
            Historical development and key milestones in Sri Lanka's waste management sector
          </CardDescription>
        </CardHeader>
        <CardContent className="space-y-6">
          {/* Category Filters */}
          <div className="space-y-3">
            <p className="text-sm font-medium text-slate-700">Filter by Category:</p>
            <div className="flex gap-2 flex-wrap">
              <Button
                variant={categoryFilter === null ? 'default' : 'outline'}
                size="sm"
                onClick={() => setCategoryFilter(null)}
              >
                All Categories
              </Button>
              {categories.length > 0 && categories.map((cat) => (
                <Button
                  key={cat}
                  variant={categoryFilter === cat ? 'default' : 'outline'}
                  size="sm"
                  onClick={() => setCategoryFilter(cat)}
                >
                  {cat}
                </Button>
              ))}
            </div>
          </div>

          {/* Timeline */}
          <div className="space-y-3">
            {filteredEvents.map((event, idx) => (
              <div
                key={idx}
                className={`${getSigColor(event.significance)} pl-4 py-3 bg-slate-50 rounded-lg hover:bg-slate-100 transition-colors cursor-pointer`}
                onClick={() =>
                  setExpandedYear(expandedYear === event.year ? null : event.year)
                }
              >
                <div className="flex items-start justify-between gap-3">
                  <div className="flex-1">
                    <div className="flex items-center gap-2 mb-1">
                      <span className="text-lg font-bold text-teal-700 min-w-12">
                        {event.year}
                      </span>
                      <Badge className={getCategoryColor(event.category)}>
                        {event.category}
                      </Badge>
                      {event.significance === 'high' && (
                        <Badge variant="destructive" className="text-xs">
                          Major
                        </Badge>
                      )}
                    </div>
                    <h4 className="font-semibold text-slate-900">{event.event}</h4>
                    {expandedYear === event.year && (
                      <p className="text-sm text-slate-600 mt-2">{event.description}</p>
                    )}
                  </div>
                  <div className="pt-1">
                    {expandedYear === event.year ? (
                      <ChevronUp className="w-5 h-5 text-slate-400" />
                    ) : (
                      <ChevronDown className="w-5 h-5 text-slate-400" />
                    )}
                  </div>
                </div>
              </div>
            ))}
          </div>

          {filteredEvents.length === 0 && (
            <div className="text-center py-8 text-slate-600">
              <p>No events found in this category.</p>
            </div>
          )}
        </CardContent>
      </Card>

      {/* Key Periods */}
      <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
        <Card>
          <CardHeader>
            <CardTitle className="text-base">Foundation Phase (1994-2005)</CardTitle>
          </CardHeader>
          <CardContent className="text-sm text-slate-600">
            <p>
              Initial planning and legislative framework establishment. The Western Province Waste
              Management Statute and creation of WMA-WP laid the groundwork for organized waste
              management.
            </p>
          </CardContent>
        </Card>

        <Card>
          <CardHeader>
            <CardTitle className="text-base">Growth Phase (2006-2020)</CardTitle>
          </CardHeader>
          <CardContent className="text-sm text-slate-600">
            <p>
              Research intensification and private sector entry. Increased focus on understanding
              waste challenges and emergence of specialized waste management companies.
            </p>
          </CardContent>
        </Card>

        <Card>
          <CardHeader>
            <CardTitle className="text-base">Modernization Phase (2021-2024)</CardTitle>
          </CardHeader>
          <CardContent className="text-sm text-slate-600">
            <p>
              Infrastructure development and technology adoption. Launch of waste-to-energy
              facility and international recognition of waste management achievements.
            </p>
          </CardContent>
        </Card>

        <Card>
          <CardHeader>
            <CardTitle className="text-base">Expansion Phase (2025-2027)</CardTitle>
          </CardHeader>
          <CardContent className="text-sm text-slate-600">
            <p>
              Scaling up initiatives and international partnerships. Multiple projects and funding
              mechanisms supporting plastic waste management and circular economy development.
            </p>
          </CardContent>
        </Card>
      </div>
    </div>
  );
}
