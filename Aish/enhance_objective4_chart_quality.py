#!/usr/bin/env python3

"""
Enhance Chart.js configurations for better pixel quality and visual clarity
"""

def enhance_chart_quality():
    """Improve Chart.js rendering quality and visual appearance"""
    
    template_path = "sustainable_energy/dashboard/templates/dashboard/objective4.html"
    
    # Read current template
    with open(template_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find and enhance the model comparison chart creation
    old_mse_chart = '''            mseChart = new Chart(ctx, {
                type: 'bar',
                data: {
                    labels: models,
                    datasets: [{
                        label: 'Mean Squared Error (MSE)',
                        data: mseValues,
                        backgroundColor: colors,
                        borderColor: borderColors,
                        borderWidth: 2
                    }]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    plugins: {
                        legend: {
                            display: false
                        },
                        title: {
                            display: true,
                            text: 'Sub-objective 4: SDG 7 Monitoring - Model Comparison (Lower MSE is Better)',
                            font: {
                                size: 16,
                                weight: 'bold'
                            }
                        }
                    },
                    scales: {
                        y: {
                            beginAtZero: true,
                            title: {
                                display: true,
                                text: 'MSE Score'
                            }
                        }
                    }
                }
            });'''
    
    new_mse_chart = '''            mseChart = new Chart(ctx, {
                type: 'bar',
                data: {
                    labels: models,
                    datasets: [{
                        label: 'Mean Squared Error (MSE)',
                        data: mseValues,
                        backgroundColor: colors,
                        borderColor: borderColors,
                        borderWidth: 0,
                        borderRadius: 8,
                        borderSkipped: false
                    }]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    devicePixelRatio: window.devicePixelRatio || 2,
                    plugins: {
                        legend: {
                            display: false
                        },
                        title: {
                            display: true,
                            text: 'Model Comparison: SDG 7 Monitoring (Lower MSE = Better Performance)',
                            font: {
                                size: 18,
                                weight: '700',
                                family: '-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif'
                            },
                            color: '#1f2937',
                            padding: 25
                        },
                        tooltip: {
                            backgroundColor: 'rgba(255, 255, 255, 0.95)',
                            titleColor: '#1f2937',
                            bodyColor: '#374151',
                            borderColor: '#e5e7eb',
                            borderWidth: 1,
                            cornerRadius: 12,
                            padding: 15,
                            titleFont: {
                                size: 14,
                                weight: '600'
                            },
                            bodyFont: {
                                size: 13,
                                weight: '500'
                            },
                            callbacks: {
                                label: function(context) {
                                    return `MSE: ${context.parsed.y.toFixed(4)}`;
                                }
                            }
                        }
                    },
                    scales: {
                        y: {
                            beginAtZero: true,
                            title: {
                                display: true,
                                text: 'Mean Squared Error (MSE)',
                                font: {
                                    size: 14,
                                    weight: '600'
                                },
                                color: '#374151'
                            },
                            grid: {
                                color: 'rgba(229, 231, 235, 0.8)',
                                lineWidth: 1
                            },
                            ticks: {
                                font: {
                                    size: 12,
                                    weight: '500'
                                },
                                color: '#6b7280'
                            }
                        },
                        x: {
                            title: {
                                display: true,
                                text: 'ML Algorithms',
                                font: {
                                    size: 14,
                                    weight: '600'
                                },
                                color: '#374151'
                            },
                            grid: {
                                display: false
                            },
                            ticks: {
                                font: {
                                    size: 12,
                                    weight: '500'
                                },
                                color: '#6b7280',
                                maxRotation: 45
                            }
                        }
                    },
                    animation: {
                        duration: 1500,
                        easing: 'easeOutQuart'
                    }
                }
            });'''
    
    content = content.replace(old_mse_chart, new_mse_chart)
    
    # Enhance the SDG 7 historical chart
    old_historical_chart = '''            historicalChart = new Chart(ctx, {
                type: 'line',
                data: {
                    labels: allYears,
                    datasets: datasets
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    plugins: {
                        legend: {
                            display: true,
                            position: 'right',
                            align: 'start',
                            maxWidth: 250,
                            labels: {
                                boxWidth: 12,
                                padding: 4,
                                font: {
                                    size: 11
                                },
                                usePointStyle: false,
                                generateLabels: function(chart) {
                                    const original = Chart.defaults.plugins.legend.labels.generateLabels;
                                    const labels = original.call(this, chart);
                                    
                                    // Sort labels alphabetically (like in the image)
                                    labels.sort((a, b) => a.text.localeCompare(b.text));
                                    
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
                            },
                            color: '#2c3e50'
                        },
                        tooltip: {
                            mode: 'index',
                            intersect: false,
                            backgroundColor: 'rgba(255, 255, 255, 0.95)',
                            titleColor: '#2c3e50',
                            bodyColor: '#2c3e50',
                            borderColor: '#ddd',
                            borderWidth: 1,
                            callbacks: {
                                title: function(tooltipItems) {
                                    return 'Year: ' + tooltipItems[0].label;
                                },
                                label: function(context) {
                                    if (context.parsed.y !== null) {
                                        return context.dataset.label + ': ' + context.parsed.y.toFixed(1) + '%';
                                    }
                                    return context.dataset.label + ': No data';
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
                                text: 'Electricity Access',
                                font: {
                                    size: 12,
                                    weight: 'bold'
                                }
                            },
                            grid: {
                                color: 'rgba(0,0,0,0.1)',
                                drawBorder: false
                            },
                            ticks: {
                                font: {
                                    size: 11
                                }
                            }
                        },
                        x: {
                            title: {
                                display: false // Hide x-axis title like in the image
                            },
                            grid: {
                                color: 'rgba(0,0,0,0.1)',
                                drawBorder: false
                            },
                            ticks: {
                                font: {
                                    size: 11
                                }
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
                    },
                    layout: {
                        padding: {
                            right: 20
                        }
                    }
                }
            });'''
    
    new_historical_chart = '''            historicalChart = new Chart(ctx, {
                type: 'line',
                data: {
                    labels: allYears,
                    datasets: datasets
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    devicePixelRatio: window.devicePixelRatio || 2,
                    plugins: {
                        legend: {
                            display: true,
                            position: 'right',
                            align: 'start',
                            maxWidth: 280,
                            labels: {
                                boxWidth: 15,
                                padding: 8,
                                font: {
                                    size: 12,
                                    weight: '500',
                                    family: '-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif'
                                },
                                color: '#374151',
                                usePointStyle: true,
                                generateLabels: function(chart) {
                                    const original = Chart.defaults.plugins.legend.labels.generateLabels;
                                    const labels = original.call(this, chart);
                                    
                                    // Sort labels alphabetically
                                    labels.sort((a, b) => a.text.localeCompare(b.text));
                                    
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
                                
                                chart.update('none');
                            }
                        },
                        title: {
                            display: true,
                            text: 'SDG 7: Access to Electricity Over Time',
                            font: {
                                size: 20,
                                weight: '700',
                                family: '-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif'
                            },
                            color: '#1f2937',
                            padding: 25
                        },
                        tooltip: {
                            mode: 'index',
                            intersect: false,
                            backgroundColor: 'rgba(255, 255, 255, 0.98)',
                            titleColor: '#1f2937',
                            bodyColor: '#374151',
                            borderColor: '#e5e7eb',
                            borderWidth: 1,
                            cornerRadius: 12,
                            padding: 15,
                            titleFont: {
                                size: 14,
                                weight: '600'
                            },
                            bodyFont: {
                                size: 13,
                                weight: '500'
                            },
                            callbacks: {
                                title: function(tooltipItems) {
                                    return 'Year: ' + tooltipItems[0].label;
                                },
                                label: function(context) {
                                    if (context.parsed.y !== null) {
                                        return context.dataset.label + ': ' + context.parsed.y.toFixed(1) + '%';
                                    }
                                    return context.dataset.label + ': No data';
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
                                text: 'Electricity Access (%)',
                                font: {
                                    size: 14,
                                    weight: '600',
                                    family: '-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif'
                                },
                                color: '#374151'
                            },
                            grid: {
                                color: 'rgba(229, 231, 235, 0.8)',
                                lineWidth: 1,
                                drawBorder: false
                            },
                            ticks: {
                                font: {
                                    size: 12,
                                    weight: '500'
                                },
                                color: '#6b7280'
                            }
                        },
                        x: {
                            title: {
                                display: false
                            },
                            grid: {
                                color: 'rgba(229, 231, 235, 0.6)',
                                lineWidth: 1,
                                drawBorder: false
                            },
                            ticks: {
                                font: {
                                    size: 12,
                                    weight: '500'
                                },
                                color: '#6b7280'
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
                    },
                    layout: {
                        padding: {
                            right: 30
                        }
                    },
                    animation: {
                        duration: 1200,
                        easing: 'easeOutQuart'
                    }
                }
            });'''
    
    content = content.replace(old_historical_chart, new_historical_chart)
    
    # Write the enhanced template
    with open(template_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("✅ Enhanced Chart.js quality and visual appearance!")
    print("\n📊 Chart Improvements:")
    print("   - High-DPI rendering (devicePixelRatio optimization)")
    print("   - Enhanced typography and font weights")
    print("   - Better color contrast and readability")
    print("   - Improved tooltips with rounded corners")
    print("   - Smoother animations and transitions")
    print("   - Better grid lines and spacing")
    print("   - Enhanced legend styling")
    print("   - Crisp bar chart borders and radius")

if __name__ == "__main__":
    enhance_chart_quality()