import { useState } from 'react';
import { Tabs, TabsContent, TabsList, TabsTrigger } from '@/components/ui/tabs';
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '@/components/ui/card';
import { Badge } from '@/components/ui/badge';
import { Button } from '@/components/ui/button';
import { MapPin, TrendingUp, AlertTriangle, Download, Globe, Building2, BarChart3, Calendar } from 'lucide-react';
import { MapView } from '@/components/Map';
import CompanyDirectory from '@/components/CompanyDirectory';
import GapAnalysisDashboard from '@/components/GapAnalysisDashboard';
import TimelineExplorer from '@/components/TimelineExplorer';

export default function Home() {
  const [activeTab, setActiveTab] = useState('overview');

  const stats = [
    { label: 'Active Companies', value: '15+', icon: Building2 },
    { label: 'Waste Sites', value: '8', icon: MapPin },
    { label: 'Lifecycle Gaps', value: '15', icon: AlertTriangle },
    { label: 'Funding (USD)', value: '$1.2M+', icon: TrendingUp },
  ];

  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-50 to-slate-100">
      {/* Header Section */}
      <header className="border-b border-slate-200 bg-white shadow-sm">
        <div className="container mx-auto px-4 py-8">
          <div className="flex items-start justify-between mb-6 gap-6">
            <div className="flex-1">
              <h1 className="text-4xl font-bold text-slate-900 mb-2">
                Sri Lanka Waste Management Ecosystem
              </h1>
              <p className="text-lg text-slate-600">
                Comprehensive data platform for waste management companies, infrastructure, initiatives, and gap analysis
              </p>
            </div>
            <Button variant="outline" size="lg" className="flex items-center gap-2 whitespace-nowrap">
              <Download className="w-4 h-4" />
              Download Data
            </Button>
          </div>

          {/* Stats Grid */}
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
            {stats.map((stat, idx) => {
              const Icon = stat.icon;
              return (
                <Card key={idx} className="bg-gradient-to-br from-teal-50 to-slate-50 border-teal-200">
                  <CardContent className="pt-6">
                    <div className="flex items-center justify-between">
                      <div>
                        <p className="text-sm text-slate-600 mb-1">{stat.label}</p>
                        <p className="text-3xl font-bold text-teal-700">{stat.value}</p>
                      </div>
                      <Icon className="w-8 h-8 text-teal-600 opacity-20" />
                    </div>
                  </CardContent>
                </Card>
              );
            })}
          </div>
        </div>
      </header>

      {/* Main Content */}
      <main className="container mx-auto px-4 py-8">
        <Tabs value={activeTab} onValueChange={setActiveTab} className="w-full">
          <TabsList className="grid w-full grid-cols-5 mb-8 bg-white border border-slate-200">
            <TabsTrigger value="overview">Overview</TabsTrigger>
            <TabsTrigger value="map">Map</TabsTrigger>
            <TabsTrigger value="companies">Companies</TabsTrigger>
            <TabsTrigger value="gaps">Gap Analysis</TabsTrigger>
            <TabsTrigger value="timeline">Timeline</TabsTrigger>
          </TabsList>

          {/* Overview Tab */}
          <TabsContent value="overview" className="space-y-6">
            <Card>
              <CardHeader>
                <CardTitle className="flex items-center gap-2">
                  <Globe className="w-5 h-5 text-teal-600" />
                  Ecosystem Overview
                </CardTitle>
                <CardDescription>
                  Comprehensive view of Sri Lanka's waste management landscape
                </CardDescription>
              </CardHeader>
              <CardContent className="space-y-6">
                <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                  <div className="bg-gradient-to-br from-amber-50 to-orange-50 p-6 rounded-lg border border-amber-200">
                    <h3 className="font-semibold text-amber-900 mb-3 flex items-center gap-2">
                      <AlertTriangle className="w-4 h-4" />
                      Critical Gaps Identified
                    </h3>
                    <ul className="space-y-2 text-sm text-amber-800">
                      <li>• Segregation at source (0% coverage)</li>
                      <li>• Treatment & processing infrastructure</li>
                      <li>• Waste-to-energy capacity (1 facility)</li>
                      <li>• Hazardous waste management</li>
                      <li>• Sustainable financing mechanisms</li>
                    </ul>
                  </div>

                  <div className="bg-gradient-to-br from-green-50 to-emerald-50 p-6 rounded-lg border border-green-200">
                    <h3 className="font-semibold text-green-900 mb-3 flex items-center gap-2">
                      <TrendingUp className="w-4 h-4" />
                      Recent Developments
                    </h3>
                    <ul className="space-y-2 text-sm text-green-800">
                      <li>• Kerawalapitiya WTE facility operational (2021)</li>
                      <li>• Kattankudy recycling centre launched (2025)</li>
                      <li>• UNDP-Coca-Cola plastic project (2024-2027)</li>
                      <li>• EU biodiversity grant (€8M, 2025)</li>
                      <li>• Clean Sri Lanka Programme expansion</li>
                    </ul>
                  </div>
                </div>

                <div className="bg-slate-50 p-6 rounded-lg border border-slate-200">
                  <h3 className="font-semibold text-slate-900 mb-4">Key Statistics</h3>
                  <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
                    <div className="text-center">
                      <p className="text-slate-600 text-sm mb-1">Local Companies</p>
                      <p className="text-3xl font-bold text-teal-700">15+</p>
                    </div>
                    <div className="text-center">
                      <p className="text-slate-600 text-sm mb-1">Dump Sites</p>
                      <p className="text-3xl font-bold text-teal-700">8</p>
                    </div>
                    <div className="text-center">
                      <p className="text-slate-600 text-sm mb-1">Active Initiatives</p>
                      <p className="text-3xl font-bold text-teal-700">8</p>
                    </div>
                    <div className="text-center">
                      <p className="text-slate-600 text-sm mb-1">Global Companies</p>
                      <p className="text-3xl font-bold text-teal-700">10+</p>
                    </div>
                  </div>
                </div>
              </CardContent>
            </Card>
          </TabsContent>

          {/* Map Tab */}
          <TabsContent value="map">
            <Card>
              <CardHeader>
                <CardTitle className="flex items-center gap-2">
                  <MapPin className="w-5 h-5 text-teal-600" />
                  Waste Management Infrastructure Map
                </CardTitle>
                <CardDescription>
                  Interactive map of dump sites, facilities, and projects across Sri Lanka
                </CardDescription>
              </CardHeader>
              <CardContent>
                <div className="h-[600px] rounded-lg overflow-hidden border border-slate-200 bg-slate-100 flex items-center justify-center">
                  <div className="text-center text-slate-600">
                    <p className="font-medium">Interactive Map</p>
                    <p className="text-sm">Waste management facilities and sites across Sri Lanka</p>
                  </div>
                </div>
              </CardContent>
            </Card>
          </TabsContent>

          {/* Companies Tab */}
          <TabsContent value="companies">
            <CompanyDirectory />
          </TabsContent>

          {/* Gap Analysis Tab */}
          <TabsContent value="gaps">
            <GapAnalysisDashboard />
          </TabsContent>

          {/* Timeline Tab */}
          <TabsContent value="timeline">
            <TimelineExplorer />
          </TabsContent>
        </Tabs>

        {/* Data Download Section */}
        <Card className="mt-12 bg-gradient-to-r from-teal-50 to-slate-50 border-teal-200">
          <CardHeader>
            <CardTitle className="flex items-center gap-2">
              <Download className="w-5 h-5 text-teal-600" />
              Download Master Datasets
            </CardTitle>
            <CardDescription>
              Access comprehensive datasets in multiple formats for analysis and research
            </CardDescription>
          </CardHeader>
          <CardContent>
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
              {[
                { name: 'Companies Directory', format: 'CSV' },
                { name: 'Waste Sites', format: 'GeoJSON' },
                { name: 'Initiatives & Funding', format: 'CSV' },
                { name: 'Gap Analysis', format: 'CSV' },
                { name: 'Timeline Data', format: 'JSON' },
                { name: 'Global Companies', format: 'CSV' },
              ].map((dataset, idx) => (
                <Button key={idx} variant="outline" className="justify-start h-auto py-3">
                  <Download className="w-4 h-4 mr-2" />
                  <div className="text-left">
                    <p className="font-medium text-sm">{dataset.name}</p>
                    <p className="text-xs text-slate-500">.{dataset.format.toLowerCase()}</p>
                  </div>
                </Button>
              ))}
            </div>
          </CardContent>
        </Card>
      </main>

      {/* Footer */}
      <footer className="border-t border-slate-200 bg-white mt-16 py-8">
        <div className="container mx-auto px-4 text-center text-sm text-slate-600">
          <p>Sri Lanka Waste Management Ecosystem Platform | Data compiled from CEA, UNDP, and industry sources</p>
          <p className="mt-2">Last updated: April 2026</p>
        </div>
      </footer>
    </div>
  );
}
