#!/usr/bin/env python3
"""
Add country search bar and analyze country button to Objective 5
"""

def add_country_analysis_objective5():
    template_path = "sustainable_energy/dashboard/templates/dashboard/objective5_classification.html"
    
    print("🔧 Adding country search bar and analyze button to Objective 5...")
    
    try:
        # Read the current template
        with open(template_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Find the model comparison section and add country analysis after it
        model_section_end = '''        </div>
    </div>
    
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>'''
        
        # Country analysis section to add
        country_section = '''        </div>
        
        <!-- Country Selection Section -->
        <div class="section-card">
            <h2 class="section-title"><i class="fas fa-globe"></i> Country Analysis</h2>
            <p class="text-muted">Select a country to analyze energy equity patterns and predictions</p>
            
            <div class="row align-items-center mb-4">
                <div class="col-md-8">
                    <select id="countrySelect" class="form-select" style="border-radius: 10px; padding: 12px 20px; border: 2px solid #e0e0e0; font-size: 1rem;">
                        <option value="">-- Select a Country --</option>
                    </select>
                </div>
                <div class="col-md-4">
                    <button class="btn w-100" onclick="analyzeCountry()" style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; border: none; padding: 12px 30px; border-radius: 10px; font-weight: bold; font-size: 1rem;">
                        <i class="fas fa-search"></i> Analyze Country
                    </button>
                </div>
            </div>
        </div>
        
        <!-- Historical Data Section -->
        <div class="section-card" id="historicalSection" style="display: none;">
            <h2 class="section-title"><i class="fas fa-history"></i> Historical Energy Equity Data</h2>
            <p class="text-muted" id="historicalCountryName"></p>
            <div class="chart-container">
                <canvas id="historicalChart"></canvas>
            </div>
        </div>
        
        <!-- Future Predictions Section -->
        <div class="section-card" id="predictionsSection" style="display: none;">
            <h2 class="section-title"><i class="fas fa-crystal-ball"></i> Energy Equity Predictions (2021-2030)</h2>
            <p class="text-muted" id="predictionsCountryName"></p>
            <div class="chart-container">
                <canvas id="predictionsChart"></canvas>
            </div>
        </div>
    </div>
    
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>'''
        
        if model_section_end in content:
            content = content.replace(model_section_end, country_section)
            print("✅ Added country selection and analysis sections")
        
        # Add JavaScript functions for country analysis
        js_functions = '''        
        let historicalChart = null;
        let predictionsChart = null;
        
        // Load countries when page loads
        window.addEventListener('load', function() {
            console.log('🌟 Page loaded, creating chart and loading countries...');
            setTimeout(createChart, 100);
            loadCountries();
        });
        
        // Load countries for dropdown
        function loadCountries() {
            console.log('📡 Loading countries...');
            fetch('/api/objective5/countries/')
                .then(response => response.json())
                .then(data => {
                    if (data.success) {
                        const select = document.getElementById('countrySelect');
                        select.innerHTML = '<option value="">-- Select a Country --</option>';
                        data.countries.forEach(country => {
                            const option = document.createElement('option');
                            option.value = country;
                            option.textContent = country;
                            select.appendChild(option);
                        });
                        console.log(`✅ Loaded ${data.countries.length} countries`);
                    }
                })
                .catch(error => {
                    console.error('❌ Error loading countries:', error);
                });
        }
        
        // Analyze selected country
        function analyzeCountry() {
            const country = document.getElementById('countrySelect').value;
            
            if (!country) {
                alert('Please select a country first!');
                return;
            }
            
            console.log(`🔍 Analyzing country: ${country}`);
            
            // Load historical data
            loadHistoricalData(country);
            
            // Load predictions
            loadPredictions(country);
        }
        
        // Load historical energy equity data
        function loadHistoricalData(country) {
            console.log(`📊 Loading historical data for ${country}`);
            
            fetch(`/api/objective5/historical/?country=${encodeURIComponent(country)}`)
                .then(response => response.json())
                .then(data => {
                    if (data.success && data.data.length > 0) {
                        document.getElementById('historicalSection').style.display = 'block';
                        document.getElementById('historicalCountryName').textContent = 
                            `Energy access trends for ${country}`;
                        
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
                                    borderColor: '#667eea',
                                    backgroundColor: 'rgba(102, 126, 234, 0.1)',
                                    borderWidth: 3,
                                    fill: true,
                                    tension: 0.4
                                }]
                            },
                            options: {
                                responsive: true,
                                maintainAspectRatio: false,
                                plugins: {
                                    legend: {
                                        display: true
                                    },
                                    title: {
                                        display: true,
                                        text: `Historical Energy Access - ${country}`,
                                        font: {
                                            size: 16,
                                            weight: 'bold'
                                        }
                                    }
                                },
                                scales: {
                                    y: {
                                        beginAtZero: true,
                                        max: 100,
                                        title: {
                                            display: true,
                                            text: 'Access to Electricity (%)'
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
                    } else {
                        console.log('No historical data available for', country);
                    }
                })
                .catch(error => {
                    console.error('❌ Error loading historical data:', error);
                });
        }
        
        // Load future predictions
        function loadPredictions(country) {
            console.log(`🔮 Loading predictions for ${country}`);
            
            fetch(`/api/objective5/predictions/?country=${encodeURIComponent(country)}&years=10`)
                .then(response => response.json())
                .then(data => {
                    if (data.success && data.predictions.length > 0) {
                        document.getElementById('predictionsSection').style.display = 'block';
                        document.getElementById('predictionsCountryName').textContent = 
                            `Predicted energy equity trends for ${country}`;
                        
                        const ctx = document.getElementById('predictionsChart').getContext('2d');
                        
                        if (predictionsChart) {
                            predictionsChart.destroy();
                        }
                        
                        const years = data.predictions.map(d => d.Year);
                        const predictions = data.predictions.map(d => d['Access to electricity (% of population)']);
                        
                        predictionsChart = new Chart(ctx, {
                            type: 'line',
                            data: {
                                labels: years,
                                datasets: [{
                                    label: 'Predicted Access (%)',
                                    data: predictions,
                                    borderColor: '#764ba2',
                                    backgroundColor: 'rgba(118, 75, 162, 0.1)',
                                    borderWidth: 3,
                                    fill: true,
                                    tension: 0.4,
                                    borderDash: [5, 5]
                                }]
                            },
                            options: {
                                responsive: true,
                                maintainAspectRatio: false,
                                plugins: {
                                    legend: {
                                        display: true
                                    },
                                    title: {
                                        display: true,
                                        text: `Future Energy Access Predictions - ${country}`,
                                        font: {
                                            size: 16,
                                            weight: 'bold'
                                        }
                                    }
                                },
                                scales: {
                                    y: {
                                        beginAtZero: true,
                                        max: 100,
                                        title: {
                                            display: true,
                                            text: 'Access to Electricity (%)'
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
                    } else {
                        console.log('No prediction data available for', country);
                    }
                })
                .catch(error => {
                    console.error('❌ Error loading predictions:', error);
                });
        }'''
        
        # Find where to insert the JavaScript functions
        js_insertion_point = '''        // Load chart immediately when page loads
        window.addEventListener('load', function() {
            console.log('🌟 Page loaded, creating chart...');
            setTimeout(createChart, 100); // Small delay to ensure everything is ready
        });'''
        
        if js_insertion_point in content:
            content = content.replace(js_insertion_point, js_functions)
            print("✅ Added JavaScript functions for country analysis")
        
        # Write back the updated content
        with open(template_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print("✅ Country analysis functionality added to Objective 5!")
        print("📝 Added features:")
        print("   - Country dropdown with all available countries")
        print("   - 'Analyze Country' button")
        print("   - Historical energy access chart")
        print("   - Future predictions chart")
        print("   - Automatic country loading on page load")
        print("🔄 Please refresh your browser to see the new functionality")
        
    except Exception as e:
        print(f"❌ Error adding country analysis: {e}")

if __name__ == "__main__":
    add_country_analysis_objective5()