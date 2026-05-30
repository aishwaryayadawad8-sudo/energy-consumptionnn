#!/usr/bin/env python3

"""
Update Objective 4 to show interactive historical chart like the provided image
All countries loaded but hidden by default, users can click legend to show/hide
"""

def update_objective4_interactive_chart():
    """Update Objective 4 template to show interactive historical chart"""
    
    template_path = "sustainable_energy/dashboard/templates/dashboard/objective4.html"
    
    # Read current template
    with open(template_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find the loadCountryData function and replace it
    old_function_start = content.find('function loadCountryData() {')
    old_function_end = content.find('function loadCountries() {')
    
    if old_function_start == -1 or old_function_end == -1:
        print("❌ Could not find loadCountryData function")
        return
    
    # New interactive chart function
    new_function = '''        function loadCountryData() {
            const country = document.getElementById('countrySelect').value;
            
            if (!country) {
                // If no country selected, load ALL countries for interactive chart
                loadAllCountriesHistoricalChart();
                return;
            }
            
            // Load specific country data
            loadSpecificCountryData(country);
        }
        
        function loadAllCountriesHistoricalChart() {
            console.log('🌍 Loading interactive historical chart for ALL countries...');
            
            // Show historical section
            document.getElementById('historicalSection').style.display = 'block';
            document.getElementById('historicalCountryName').textContent = 
                'SDG 7: Access to Electricity Over Time (Click legend to show/hide countries)';
            
            // Get all countries first
            fetch('/api/objective4/countries/')
                .then(response => response.json())
                .then(countriesData => {
                    if (countriesData.success) {
                        const countries = countriesData.countries;
                        console.log(`📊 Loading data for ${countries.length} countries...`);
                        
                        // Load historical data for all countries
                        const promises = countries.map(country => 
                            fetch(`/api/objective4/historical/?country=${encodeURIComponent(country)}`)
                                .then(response => response.json())
                                .then(data => ({
                                    country: country,
                                    data: data.success ? data.data : []
                                }))
                                .catch(error => ({
                                    country: country,
                                    data: []
                                }))
                        );
                        
                        Promise.all(promises).then(allCountryData => {
                            createInteractiveHistoricalChart(allCountryData);
                        });
                    }
                })
                .catch(error => console.error('Error loading countries:', error));
        }
        
        function createInteractiveHistoricalChart(allCountryData) {
            console.log('📈 Creating interactive historical chart...');
            
            const ctx = document.getElementById('historicalChart').getContext('2d');
            
            if (historicalChart) {
                historicalChart.destroy();
            }
            
            // Prepare datasets for all countries
            const datasets = [];
            const colors = [
                'rgba(255, 99, 132, 0.8)',   // Red
                'rgba(54, 162, 235, 0.8)',   // Blue  
                'rgba(255, 205, 86, 0.8)',   // Yellow
                'rgba(75, 192, 192, 0.8)',   // Teal
                'rgba(153, 102, 255, 0.8)',  // Purple
                'rgba(255, 159, 64, 0.8)',   // Orange
                'rgba(199, 199, 199, 0.8)',  // Grey
                'rgba(83, 102, 255, 0.8)',   // Indigo
                'rgba(255, 99, 255, 0.8)',   // Pink
                'rgba(99, 255, 132, 0.8)'    // Green
            ];
            
            allCountryData.forEach((countryInfo, index) => {
                if (countryInfo.data && countryInfo.data.length > 0) {
                    const years = countryInfo.data.map(d => d.Year);
                    const access = countryInfo.data.map(d => d['Access to electricity (% of population)']);
                    
                    datasets.push({
                        label: countryInfo.country,
                        data: access,
                        borderColor: colors[index % colors.length],
                        backgroundColor: colors[index % colors.length].replace('0.8', '0.1'),
                        borderWidth: 2,
                        fill: false,
                        tension: 0.1,
                        pointRadius: 3,
                        pointHoverRadius: 5,
                        hidden: index > 0  // Hide all except first country by default
                    });
                }
            });
            
            // Get years from first country (assuming all have similar year ranges)
            const firstCountryWithData = allCountryData.find(c => c.data && c.data.length > 0);
            const years = firstCountryWithData ? firstCountryWithData.data.map(d => d.Year) : [];
            
            historicalChart = new Chart(ctx, {
                type: 'line',
                data: {
                    labels: years,
                    datasets: datasets
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    plugins: {
                        legend: {
                            display: true,
                            position: 'right',
                            labels: {
                                boxWidth: 12,
                                padding: 8,
                                font: {
                                    size: 11
                                },
                                generateLabels: function(chart) {
                                    const original = Chart.defaults.plugins.legend.labels.generateLabels;
                                    const labels = original.call(this, chart);
                                    
                                    // Add click handler info
                                    labels.forEach(label => {
                                        label.text = label.text + (label.hidden ? ' (hidden)' : '');
                                    });
                                    
                                    return labels;
                                }
                            },
                            onClick: function(e, legendItem, legend) {
                                const index = legendItem.datasetIndex;
                                const chart = legend.chart;
                                
                                if (chart.isDatasetVisible(index)) {
                                    chart.hide(index);
                                    legendItem.hidden = true;
                                } else {
                                    chart.show(index);
                                    legendItem.hidden = false;
                                }
                                
                                chart.update();
                            }
                        },
                        title: {
                            display: true,
                            text: 'SDG 7: Access to Electricity Over Time',
                            font: {
                                size: 16,
                                weight: 'bold'
                            }
                        },
                        tooltip: {
                            mode: 'index',
                            intersect: false,
                            callbacks: {
                                title: function(tooltipItems) {
                                    return 'Year: ' + tooltipItems[0].label;
                                },
                                label: function(context) {
                                    return context.dataset.label + ': ' + context.parsed.y.toFixed(1) + '%';
                                }
                            }
                        }
                    },
                    scales: {
                        y: {
                            beginAtZero: true,
                            max: 100,
                            title: {
                                display: true,
                                text: 'Electricity Access (%)'
                            },
                            grid: {
                                color: 'rgba(0,0,0,0.1)'
                            }
                        },
                        x: {
                            title: {
                                display: true,
                                text: 'Year'
                            },
                            grid: {
                                color: 'rgba(0,0,0,0.1)'
                            }
                        }
                    },
                    interaction: {
                        mode: 'nearest',
                        axis: 'x',
                        intersect: false
                    },
                    hover: {
                        mode: 'nearest',
                        intersect: false
                    }
                }
            });
            
            console.log(`✅ Interactive chart created with ${datasets.length} countries`);
            console.log('💡 Click legend items to show/hide countries');
        }
        
        function loadSpecificCountryData(country) {
            console.log(`🔍 Loading specific data for: ${country}`);
            
            // Load historical data for specific country
            fetch(`/api/objective4/historical/?country=${encodeURIComponent(country)}`)
                .then(response => response.json())
                .then(data => {
                    if (data.success && data.data.length > 0) {
                        document.getElementById('historicalSection').style.display = 'block';
                        document.getElementById('historicalCountryName').textContent = 
                            `Electricity access trends for ${country}`;
                        
                        const ctx = document.getElementById('historicalChart').getContext('2d');
                        
                        if (historicalChart) {
                            historicalChart.destroy();
                        }
                        
                        const years = data.data.map(d => d.Year);
                        const access = data.data.map(d => d['Access to electricity (% of population)']);
                        
                        historicalChart = new Chart(ctx, {
                            type: 'line',
                            data: {
                                labels: years,
                                datasets: [{
                                    label: 'Electricity Access (%)',
                                    data: access,
                                    borderColor: 'rgba(102, 126, 234, 1)',
                                    backgroundColor: 'rgba(102, 126, 234, 0.1)',
                                    borderWidth: 3,
                                    fill: true,
                                    tension: 0,
                                    pointRadius: 5,
                                    pointHoverRadius: 7
                                }]
                            },
                            options: {
                                responsive: true,
                                maintainAspectRatio: false,
                                plugins: {
                                    legend: {
                                        display: true
                                    }
                                },
                                scales: {
                                    y: {
                                        beginAtZero: true,
                                        max: 100,
                                        title: {
                                            display: true,
                                            text: 'Access (%)'
                                        }
                                    },
                                    x: {
                                        title: {
                                            display: true,
                                            text: 'Year'
                                        }
                                    }
                                }
                            }
                        });
                    }
                })
                .catch(error => console.error('Error loading historical data:', error));
            
            // Load predictions for specific country
            fetch(`/api/objective4/predictions/?country=${encodeURIComponent(country)}&years=7`)
                .then(response => response.json())
                .then(data => {
                    if (data.success && data.predictions.length > 0) {
                        document.getElementById('predictionsSection').style.display = 'block';
                        document.getElementById('predictionsCountryName').textContent = 
                            `Predicted electricity access for ${country}`;
                        
                        const ctx = document.getElementById('predictionsChart').getContext('2d');
                        
                        if (predictionsChart) {
                            predictionsChart.destroy();
                        }
                        
                        const years = data.predictions.map(d => d.year);
                        const predictions = data.predictions.map(d => d.predicted_access);
                        
                        predictionsChart = new Chart(ctx, {
                            type: 'line',
                            data: {
                                labels: years,
                                datasets: [{
                                    label: 'Predicted Access (%)',
                                    data: predictions,
                                    borderColor: 'rgba(39, 174, 96, 1)',
                                    backgroundColor: 'rgba(39, 174, 96, 0.1)',
                                    borderWidth: 3,
                                    fill: true,
                                    tension: 0,
                                    pointRadius: 5,
                                    pointHoverRadius: 7,
                                    borderDash: [5, 5]
                                }]
                            },
                            options: {
                                responsive: true,
                                maintainAspectRatio: false,
                                plugins: {
                                    legend: {
                                        display: true
                                    }
                                },
                                scales: {
                                    y: {
                                        beginAtZero: true,
                                        max: 100,
                                        title: {
                                            display: true,
                                            text: 'Access (%)'
                                        }
                                    },
                                    x: {
                                        title: {
                                            display: true,
                                            text: 'Year'
                                        }
                                    }
                                }
                            }
                        });
                    }
                })
                .catch(error => console.error('Error loading predictions:', error));
        }
        
        '''
    
    # Replace the function
    content = content[:old_function_start] + new_function + content[old_function_end:]
    
    # Update the country selection section to include "Show All Countries" option
    old_country_section = '''            <div class="row">
                <div class="col-md-8">
                    <select id="countrySelect" class="form-select country-select">
                        <option value="">Loading countries...</option>
                    </select>
                </div>
                <div class="col-md-4">
                    <button class="btn btn-load w-100" onclick="loadCountryData()">
                        <i class="fas fa-search"></i> Analyze Country
                    </button>
                </div>
            </div>'''
    
    new_country_section = '''            <div class="row">
                <div class="col-md-8">
                    <select id="countrySelect" class="form-select country-select">
                        <option value="">-- Show All Countries (Interactive) --</option>
                    </select>
                </div>
                <div class="col-md-4">
                    <button class="btn btn-load w-100" onclick="loadCountryData()">
                        <i class="fas fa-chart-line"></i> Load Chart
                    </button>
                </div>
            </div>
            <div class="row mt-2">
                <div class="col-12">
                    <small class="text-muted">
                        💡 <strong>Tip:</strong> Select "Show All Countries" to see interactive chart, or choose specific country for detailed analysis
                    </small>
                </div>
            </div>'''
    
    content = content.replace(old_country_section, new_country_section)
    
    # Update the section description
    old_description = '''            <p class="text-muted">View historical data and future predictions for a specific country</p>'''
    new_description = '''            <p class="text-muted">Interactive chart with all countries OR detailed analysis for specific country</p>'''
    
    content = content.replace(old_description, new_description)
    
    # Write the updated template
    with open(template_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("✅ Updated Objective 4 with interactive historical chart!")
    print("\n📊 New Features:")
    print("   - Interactive chart showing ALL countries")
    print("   - Countries hidden by default (legendonly)")
    print("   - Click legend to show/hide specific countries")
    print("   - Matches the style from your provided image")
    print("   - Option to analyze specific country in detail")
    print("\n🎮 User Experience:")
    print("   1. Default: 'Show All Countries' loads interactive chart")
    print("   2. Click legend items to show/hide countries")
    print("   3. Select specific country for detailed analysis")
    print("   4. Get both historical trends and future predictions")

if __name__ == "__main__":
    update_objective4_interactive_chart()