import { useState } from 'react';
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '@/components/ui/card';
import { Badge } from '@/components/ui/badge';
import { Input } from '@/components/ui/input';
import { Button } from '@/components/ui/button';
import { Search, MapPin, Users, Globe } from 'lucide-react';

const companies = [
  {
    id: 1,
    name: 'MAC Holdings (Private) Limited',
    location: 'Colombo',
    type: 'Private',
    employees: '251-500',
    founded: 1996,
    focus: 'Waste Management',
    services: 'Supply chain management and logistics',
    status: 'Active',
  },
  {
    id: 2,
    name: 'INFINITY GREEN INTERNATIONAL PVT LTD',
    location: 'Gonawala',
    type: 'Private',
    employees: '11-50',
    founded: 2019,
    focus: 'E-Waste Recycling',
    services: 'E-waste collection and recycling',
    status: 'Licensed & ISO-Certified',
  },
  {
    id: 3,
    name: 'Ceylon Waste Management Refinery (Pvt) Ltd',
    location: 'Karunaswake',
    type: 'Private',
    employees: 'N/A',
    founded: null,
    focus: 'E-Waste Management',
    services: 'E-waste collection and disposal',
    status: 'BOI Approved',
  },
  {
    id: 4,
    name: 'Success Environmental Engineering Solutions',
    location: 'Matara',
    type: 'Private',
    employees: '11-50',
    founded: 2015,
    focus: 'Environmental Services',
    services: 'Solid waste management and wastewater treatment',
    status: 'Active',
  },
  {
    id: 5,
    name: 'DAW Corporation',
    location: 'Sri Jayawardenepura Kotte',
    type: 'Private',
    employees: '51-100',
    founded: null,
    focus: 'Waste-to-Energy',
    services: 'Wastewater treatment and waste-to-energy systems',
    status: 'Active',
  },
  {
    id: 6,
    name: 'INSEE Ecocycle',
    location: 'Sri Lanka',
    type: 'Private',
    employees: 'N/A',
    founded: null,
    focus: 'Waste Management',
    services: 'Professional waste management services',
    status: 'Active',
  },
  {
    id: 7,
    name: 'Waste Management Authority of Western Province',
    location: 'Colombo',
    type: 'Government',
    employees: 'N/A',
    founded: 2005,
    focus: 'Waste Management',
    services: 'Regulation and implementation',
    status: 'Active',
  },
  {
    id: 8,
    name: 'Central Environmental Authority',
    location: 'Battaramulla',
    type: 'Government',
    employees: 'N/A',
    founded: null,
    focus: 'Environmental Regulation',
    services: 'Authorization and monitoring',
    status: 'Active',
  },
];

export default function CompanyDirectory() {
  const [searchTerm, setSearchTerm] = useState('');
  const [typeFilter, setTypeFilter] = useState<string | null>(null);

  const filteredCompanies = companies.filter((company) => {
    const matchesSearch =
      company.name.toLowerCase().includes(searchTerm.toLowerCase()) ||
      company.focus.toLowerCase().includes(searchTerm.toLowerCase()) ||
      company.location.toLowerCase().includes(searchTerm.toLowerCase());

    const matchesType = !typeFilter || company.type === typeFilter;

    return matchesSearch && matchesType;
  });

  const getStatusColor = (status: string) => {
    if (status.includes('ISO') || status.includes('BOI')) return 'bg-green-100 text-green-800';
    if (status === 'Active') return 'bg-teal-100 text-teal-800';
    return 'bg-slate-100 text-slate-800';
  };

  return (
    <div className="space-y-6">
      <Card>
        <CardHeader>
          <CardTitle>Waste Management Companies Directory</CardTitle>
          <CardDescription>
            Local and international waste management companies operating in Sri Lanka
          </CardDescription>
        </CardHeader>
        <CardContent className="space-y-6">
          {/* Filters */}
          <div className="space-y-4">
            <div className="relative">
              <Search className="absolute left-3 top-3 w-4 h-4 text-slate-400" />
              <Input
                placeholder="Search by company name, focus area, or location..."
                value={searchTerm}
                onChange={(e) => setSearchTerm(e.target.value)}
                className="pl-10"
              />
            </div>

            <div className="flex gap-2 flex-wrap">
              <Button
                variant={typeFilter === null ? 'default' : 'outline'}
                size="sm"
                onClick={() => setTypeFilter(null)}
              >
                All Types
              </Button>
              <Button
                variant={typeFilter === 'Private' ? 'default' : 'outline'}
                size="sm"
                onClick={() => setTypeFilter('Private')}
              >
                Private
              </Button>
              <Button
                variant={typeFilter === 'Government' ? 'default' : 'outline'}
                size="sm"
                onClick={() => setTypeFilter('Government')}
              >
                Government
              </Button>
            </div>
          </div>

          {/* Results Count */}
          <div className="text-sm text-slate-600">
            Showing {filteredCompanies.length} of {companies.length} companies
          </div>

          {/* Company Cards */}
          <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
            {filteredCompanies.map((company) => (
              <Card key={company.id} className="hover:shadow-md transition-shadow">
                <CardContent className="pt-6">
                  <div className="space-y-3">
                    <div className="flex items-start justify-between gap-2">
                      <h3 className="font-semibold text-slate-900 text-sm leading-tight">
                        {company.name}
                      </h3>
                      <Badge className={getStatusColor(company.status)} variant="secondary">
                        {company.status}
                      </Badge>
                    </div>

                    <div className="space-y-2 text-sm">
                      <div className="flex items-center gap-2 text-slate-600">
                        <MapPin className="w-4 h-4 text-teal-600" />
                        {company.location}
                      </div>

                      <div className="flex items-center gap-2 text-slate-600">
                        <Users className="w-4 h-4 text-teal-600" />
                        {company.employees} employees
                      </div>

                      {company.founded && (
                        <div className="text-slate-600">
                          Founded: {company.founded}
                        </div>
                      )}
                    </div>

                    <div className="pt-2 border-t border-slate-200">
                      <p className="text-xs font-medium text-slate-700 mb-1">Focus Area</p>
                      <Badge variant="outline" className="text-teal-700 border-teal-200">
                        {company.focus}
                      </Badge>
                    </div>

                    <div>
                      <p className="text-xs font-medium text-slate-700 mb-1">Services</p>
                      <p className="text-xs text-slate-600">{company.services}</p>
                    </div>
                  </div>
                </CardContent>
              </Card>
            ))}
          </div>

          {filteredCompanies.length === 0 && (
            <div className="text-center py-8 text-slate-600">
              <p>No companies found matching your criteria.</p>
            </div>
          )}
        </CardContent>
      </Card>

      {/* Global Companies Section */}
      <Card>
        <CardHeader>
          <CardTitle className="flex items-center gap-2">
            <Globe className="w-5 h-5 text-teal-600" />
            Global Waste Management Companies
          </CardTitle>
          <CardDescription>
            International companies with operations accessible to Sri Lanka
          </CardDescription>
        </CardHeader>
        <CardContent>
          <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
            {[
              {
                name: 'Waste Management Inc.',
                hq: 'USA',
                revenue: '$22.1B',
                services: 'Collection, Recycling, Disposal, WTE',
              },
              {
                name: 'Veolia',
                hq: 'France',
                revenue: '€44.4B',
                services: 'Water, Waste, Energy Management',
              },
              {
                name: 'SUEZ',
                hq: 'France',
                revenue: 'N/A',
                services: 'Water, Waste Management',
              },
              {
                name: 'Biffa',
                hq: 'UK',
                revenue: 'N/A',
                services: 'Waste Collection, Recycling',
              },
            ].map((company, idx) => (
              <Card key={idx} className="bg-slate-50 border-slate-200">
                <CardContent className="pt-6">
                  <h4 className="font-semibold text-slate-900 mb-2">{company.name}</h4>
                  <div className="space-y-1 text-sm text-slate-600">
                    <p><span className="font-medium">HQ:</span> {company.hq}</p>
                    <p><span className="font-medium">Revenue:</span> {company.revenue}</p>
                    <p><span className="font-medium">Services:</span> {company.services}</p>
                  </div>
                </CardContent>
              </Card>
            ))}
          </div>
        </CardContent>
      </Card>
    </div>
  );
}
