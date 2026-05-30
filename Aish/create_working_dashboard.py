#!/usr/bin/env python3
"""
Create a complete working explore dashboard
"""

import os

def create_working_dashboard():
    """Create a complete working explore dashboard"""
    
    index_path = "sustainable_energy/dashboard/templates/dashboard/index.html"
    
    print("🔄 Creating complete working dashboard...")
    print(f"📁 Creating file: {index_path}")
    
    # Ensure directory exists
    os.makedirs(os.path.dirname(index_path), exist_ok=True)
    
    try:
        # Complete working dashboard HTML
        dashboard_html = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Explore Dashboard - SDG 7 Energy Analytics</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
    
    <style>
        body {
            font-family: Arial, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            padding: 20px 0;
        }
        
        .dashboard-container {
            max-width: 1400px;
            margin: 0 auto;
        }
        
        .header-section {
            background: white;
            border-radius: 15px;
            padding: 30px;
            margin-bottom: 30px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.2);
            text-align: center;
        }
        
        .search-section {
            background: white;
            border-radius: 15px;
            padding: 25px;
            margin-bottom: 30px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.2);
        }
        
        #map {
            height: 500px;
            border-radius: 15px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.2);
            margin-bottom: 30px;
        }
        
        .result-section {
            background: white;
            border-radius: 15px;
            padding: 30px;
            margin-top: 30px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.2);
        }
        
        .chart-container {
            height: 400px;
            margin: 20px 0;
            background: white;
            border-radius: 10px;
            padding: 20px;
            box-shadow: 0 5px 15px rgba(0,0,0,0.1);
        }
        
        .metric-cards {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 20px;
            margin-bottom: 30px;
        }
        
        .metric-card {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            border-radius: 15px;
            padding: 25px;
            text-align: center;
        }
        
        .metric-card .value {
            font-size: 2.5rem;
            font-weight: bold;
            margin: 10px 0;
        }
        
        .search-suggestions {
            position: absolute;
            top: 100%;
            left: 0;
            right: 0;
            background: white;
            border: 1px solid #e0e0e0;
            border-radius: 8px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.1);
            z-index: 1000;
            max-height: 300px;
            overflow-y: auto;
            display: none;
        }
    </style>
</head>
<body>
    <div class="dashboard-container">
        <!-- Header Section -->
        <div class="header-section">
            <h1><i class="fas fa-search"></i> Explore Dashboard</h1>
            <p>Interactive Country Energy Analysis</p>
            <a href="/country-forecasts/" class="btn btn-secondary">
                <i class="fas fa-arrow-left"></i> Back
            </a>
        </div>

        <!-- Search Section -->
        <div class="search-section">
            <h3><i class="fas fa-globe"></i> Country Energy Analysis</h3>
            
            <div class="row">
                <!-- Search Input Column -->
                <div class="col-md-5">
                    <label for="countryInput" class="form-label">
                        <i class="fas fa-search"></i> Search Country
                    </label>
                    <div style="position: relative;">
                        <input type="text" id="countryInput" class="form-control" 
                               placeholder="Type country name..." 
                               autocomplete="off"
                               style="border-radius: 8px; padding: 12px;">
                        <div id="searchSuggestions" class="search-suggestions"></div>
                    </div>
                </div>
                
                <!-- Dropdown Column -->
                <div class="col-md-5">
                    <label for="countrySelect" class="form-label">
                        <i class="fas fa-list"></i> Select Country
                    </label>
                    <select id="countrySelect" class="form-select" 
                            style="border-radius: 8px; padding: 12px;">
                        <option value="">-- Choose a Country --</option>
                    </select>
                </div>
                
                <!-- Button Column -->
                <div class="col-md-2">
                    <label class="form-label" style="opacity: 0;">Button</label>
                    <button class="btn btn-primary w-100" onclick="analyzeSelectedCountry()" 
                            style="border-radius: 8px; padding: 12px;">
                        <i class="fas fa-search"></i> Analyze
                    </button>
                </div>
            </div>
        </div>

        <!-- World Map -->
        <div id="map"></div>

        <!-- Results Section -->
        <div class="result-section" id="resultSection" style="display: none;">
            <h2 id="countryTitle">Country Analysis</h2>
            
            <!-- Metric Cards -->
            <div class="metric-cards" id="metricCards">
                <div class="metric-card">
                    <h4>Electricity Access</h4>
                    <div class="value">--</div>
                    <div class="unit">%</div>
                </div>
                <div class="metric-card">
                    <h4>CO₂ Emissions</h4>
                    <div class="value">--</div>
                    <div class="unit">Mt</div>
                </div>
                <div class="metric-card">
                    <h4>Renewable Potential</h4>
                    <div class="value">--</div>
                    <div class="unit">%</div>
                </div>
                <div class="metric-card">
                    <h4>Energy Efficiency</h4>
                    <div class="value">--</div>
                    <div class="unit">Score</div>
                </div>
            </div>
            
            <!-- Charts -->
            <div class="cha   main()_":
 _main_ "_ __name__ ==ed.")

ifreation fail\n❌ C"rint(
        pe:    els 
")
       IONAL!FUNCT FULLY HBOARDDASn🎯 rint("\
        p     
   hboard!")the das"   3. Try    print(")
     t:8000/calhos http://lo 2. Open:rint("      p   
 r")py runserveanage.: python mvertart ser 1. S print("    
     to Test:")n🚀 Ready t("\prin        
        yling")
 strofessional ✅ P("  nt        pri")
 statisticss withrdric cat("   ✅ Met  prin)
      ts"ve char 4 interacti   ✅   print("")
     untry datah coers wit Pin mark ✅  "  print(     ting")
 ighuntry highlreen coht g"   ✅ Ligint(
        prap")rld mctive wo✅ Intera"         print(  ")
ountries 70+ cn withtry dropdow   ✅ Counnt("        pri")
suggestions live  withearch input("   ✅ Snt
        pris:")tureFeaDashboard "\n🎯  print(
       "=" * 60)  print(   ")
    CREATED!SHBOARD EXPLORE DA"✅ COMPLETE     print( 60)
    + "=" *("\n"       print
 ess:f succ 
    i
   oard()_dashbe_workingcreat success =     
)
   ("=" * 60  printD")
  G DASHBOARRKINOMPLETE WO CREATING C   print("🔄"""
 onnctifu""Main "    f main():
False

deeturn       r
  {e}")board: shating dare"❌ Error c(fprint       e:
  n as Exceptio   except   
  True
          returnd!")
   ardashboworking ed complete  createssfullyuccnt("✅ S     pri       
   
 _html)rdshboadarite(        f.wf:
    -8') as tfcoding='uenw', ex_path, 'pen(ind    with o   e file
 rd to thoaete dashbe compl # Write th  
             
</html>'''body>
ript>
</
    </sc  }e;
      countryNam    return   
                     }
      );
   ame}`untryN${corch input: sing seaole.log(`🔍 U        cons
        ;rim()alue.t.vcountryInputyName = ntr cou              ()) {
 .value.trimcountryInputput && ryInse if (count    } el       e}`);
 ryNamuntion: ${cown selectopdong drUsile.log(`🔽 nsoco        ;
        Select.value = countryountryName    c          
  lue) {elect.vayS& countrct &countrySele if (             
         '';
   =ame countryN      letlue
      ut va then inpection,own sel dropdPriority: // 
                      ');
 electryS'countId(lementBynt.getE documet =untrySelec  const co        ut');
  ('countryInptElementByIdt.ge= document yInpuuntronst co    c    ) {
    ctedCountry(Seletion get        func  

             }
 ame);untryNon(cosSectiowResult  sh      
    nsectio results ow // Also sh         
         
     Name);nMap(countrytCountryOghhli hig      map
     ntry on  coulight theately high Immedi  //            
    
                }
       return;      ;
     .`)her countrye try anotble. Pleas availame} data notountryNa ${c`Error:      alert(     
     base`);atat found in dName} noryy ${countuntrected co`❌ Selerror( console.              
 ) {e]s[countryNamrdinate!countryCoo  if (         exists
  country ify     // Ver          
 );
        ame}`{countryN $ed:try selectoung(`🎯 Csole.lo         con    
         e';
  splay = 'nonns.style.diggestions) searchSuSuggestio if (search       
    Name;ue = countryt.vallecrySe countySelect)  if (countr      me;
     = countryNaput.valuecountryIntryInput)   if (coun        wn
  dodrop input and e bothdat   // Up        
             ns');
chSuggestiod('searementByI.getEl = documentestionshSuggrcst sea   con
         ;t')ecelId('countryStByenemnt.getEl= documeySelect ntr cou   const       ut');
  InpId('countryElementByent.gett = documryInpucount    const          {
ountryName)mSearch(cuntryFroselectCoion  funct   
         }
     n`);
      opdowries to drh} countntries.lengtllCouded ${a(`✅ Adlogle.  conso
                        });
  ;
        (option)Childend.apprySelect     count         try;
  unnt = co.textConteoption            ;
    trycounlue = tion.va       op       on');
  ment('optireateEle= document.con pti    const o         y => {
   ountrach(corEries.funt   allCo     option
    s an ch country add ea/ A        /   
           .sort();
  inates)Coordtryeys(coun= Object.klCountries  al  const           sort them
ies and countr all  // Get         
            on>';
 try --</opti a Coun">-- Choosevalue="<option erHTML = 't.innountrySelec         clder)
   st placehoir the fions (exceptexisting opt/ Clear         /   
            ..');
  dropdown.countryg in🔽 Populatsole.log('   con             
   urn;
     ect) reteltryS  if (!coun      t');
    trySelecntById('counmetEleument.geelect = docnst countryS        cown() {
    ropdountryDopulateCoion pct
        fun
          }
           };
       :`, error)ntryName}courts for ${endering charor rror(`❌ Er console.er         
      r) { (erro catch      }         
       
      ;tryName}`)un{cor $sfully focesed sucs renderrtchaAll log(`✅ le.      conso
          
});               lse
 deBar: faisplayMo        d            : true,
ponsiveres                  t, { 
  ayoubleLenewae], rTrac, renewablecebaselineTraeChart', [ewablrenlot('lotly.newP           P};

                   0 }
  b: 50, l: 6, 0, r: 30n: { t: 5argi        m     
        'white',gcolor:r_b       pape       a',
      fafafgcolor: '#  plot_b                  
    },          
       100] range: [0,                ',
       '#f0f0f0idcolor:       gr                 
  Share (%)',Renewableitle: '           t         { 
        yaxis:              ,
       }              f0'
  : '#f0f0   gridcolor                    r',
 e: 'Yea     titl                   is: { 
       xax          
             },      }
     r: '#333'e: 16, colo{ siz      font:          
         ast`,Growth Forecble Energy - RenewayName}  `${countrtext:                     
    {e:     titl            
   = {ayout leL renewab const           ;

            }    p'
     'skierinfo:        hov       lse,
     gend: fashowle               },
     nt' ranspareolor: 'te: { c         lin         'lines',
  ode:          m           
r',catte'spe: ty                   
 ),p(() => 0rs.maeYeaenewabl      y: r              s,
enewableYear   x: r            
     ce = {elineTraasonst b      c        baseline
     // Add              

          };
      0, 0.1)' 6gba(231, 76,'r: color      fill            onexty',
   fill: 't                  : 8 },
 3c', size'#e74clor: marker: { co                  
  'spline' },, shape: dth: 3, wi: '#e74c3c'color: {        line             are',
enewable Sh name: 'R                   ,
+markers'nesli ' mode:                  
 : 'scatter',   type                ata,
 eDy: renewabl            s,
        wableYear   x: rene          = {
       bleTrace wast rene         con     
        });
          
 - 1);() * 2dom+ Math.ran21) * 2.5 - 20year ble + (enewa95, baseRath.min(   return M                 );
cess * 0.3)rds.ac, 20 + (cooin(80e = Math.mwablseRene banst   co           > {
      s.map(year =eYearnewabl reta =renewableDanst         co);
        21 + ii) => 20(_, 0}, length: 1om({ Array.freYears =renewabl  const             hart
  rgy Growth Cable Ene. Renew 4     //          });

                  false
yModeBar:  displa       
           e,truresponsive:                 
    yout, { tLaecas], fororecastTrace [f',sChart'accesnewPlot(    Plotly.           };

                  }
 l: 60 30, b: 50,50, r:rgin: { t:      ma            
   white', 'color:er_bg      pap          ,
    '#fafafa'or: col_bg  plot               },
                00]
       [0, 1  range:               ',
        f0f0 '#f0lor:   gridco                 
    ss (%)',itle: 'Acce   t             { 
        :      yaxis                   },
                0f0f0'
lor: '#fgridco                     r',
   'Yea:        title          
        xaxis: {                         },
           333' }
    lor: '#6, co { size: 1  font:                      )`,
0301-2recast (202Access Foy ElectricitName} - ${countryext: `    t             {
         title:                 
  out = {astLayec  const for    
          };
            ast'
    name: 'Forec           ,
                    }
         th: 1 }54', widr: '#2299line: { colo                    .8,
    city: 0opa                        e60',
27a color: '#                   : { 
    marker           
         bar', type: '             ata,
      orecastD  y: f                 rs,
 Yearecast       x: fo          
    = {stTracet foreca  cons            });

                75);
   * 1.5 - 0.h.random()1.2 + Mat) *  2021ss + (year - coords.acceh.min(100, return Mat             {
       p(year =>s.maecastYearorcastData = fst forecon      
          + i);21 i) => 20: 10}, (_, from({lengthy.ra ArecastYears =nst for       co       Chart
   castccess Fore     // 3. A    

                });    e
   deBar: falsplayMo         dis       ue,
    ive: trrespons                    Layout, { 
iee], ppieTracrt', [lot('pieChay.newP      Plotl          };

                    }
             -0.1
     y:                    enter',
   r: 'c      xancho                 5,
    x: 0.              ',
       'hation:   orient             
          legend: {                ue,
   d: trgenhowle      s           ,
   : 30 }30, l: 50, r: 30, brgin: { t:        ma            e',
 hitolor: 'w  paper_bgc               fafa',
   gcolor: '#fa      plot_b           
    },               33' }
     color: '#3 16, { size:    font:               
     bution`,urce DistriSorgy Name} - Eneountry`${c     text:                  {
    title:               
    ayout = {  const pieL          
    ;
     }          0.3
  le:       ho      e',
        'outsidposition: text              
     +percent',: 'labelnfo    texti            
          },            }
  th: 2 fff', widlor: '#ine: { co  l                     '],
 59b68db', '#9b', '#349c', '#27ae60: ['#e74c3  colors                { 
          marker:             
    pie',     type: '              ,
 ']', 'OtherearclNunewables', 'els', 'Resil Fu: ['Fos   labels              e],
   therSharrShare, ouclealeShare, nrenewabsilShare, : [fos   values       
          Trace = { pie const               Share);

e - nuclearbleSharare - renewalSh00 - fossix(0, 1th.maMaare = nst otherSh       co;
         ))hare * 0.2 (renewableS, 15 -= Math.max(5are uclearSht n   cons           hare);
  ewableS- ren75 .max(20, = Mathhare lSst fossi  con            );
  s * 0.4)coords.acces5 + (0, 1min(6h.are = MatrenewableSh   const             Chart
 ix Pie 2. Energy M      //        });

            se
       : faldeBar   displayMo                 ,
e: trueponsiv      res          ut, { 
    yo timelineLaace],ineTrimelnChart', [tPlot('mai  Plotly.new      
            };
             }
l: 60b: 50, , r: 30, : { t: 50     margin       
        e',: 'whitorcol   paper_bg                ,
  '#fafafa'r:bgcoloot_       pl           
     },               100]
   ge: [0, ran                    0f0f0',
   '#flor:      gridco                  %)',
 ccess (lectricity A  title: 'E                    is: { 
       yax      
         ,      }      
        0f0f0''#f: gridcolor                   ar',
     Ye  title: '               
       xaxis: {                       },
               
    }'#333'or: col{ size: 16,     font:             
        0)`,ne (2000-202ss Timelicity Acceriectame} - El `${countryN   text:               : {
        title                yout = {
  lineLame   const ti      

       ;           } 6 }
     b', size:or: '#3498d{ col   marker:             },
     width: 3 ', : '#3498db{ colorne:   li                Access`,
  me} Nantryme: `${cou    na           ,
     kers's+mar: 'line   mode            ',
     teratype: 'sc         t         
  ccessData, a         y:        ears,
   x: y                  e = {
  timelineTracst          con      
 );
 }                }
              1);
       -om() * 2+ Math.rand1) * 0.5 ear - 202(yess + ds.acc0, coorMath.min(10return                         ions
jectro ptureFu//                   {
            } else            5);
   - 1.) * 3 random(+ Math.000) * 0.7 year - 2 15 + (ccess -, coords.a(0.maxMath     return                 
   e variationa with som datoricalist H   //                  020) {
   ar <= 2      if (ye            {
  (year =>  = years.maptassDacce const a              00 + i);
 i) => 2021}, (_, : gth.from({lenArrayars =  const ye             Trends
   ty Accessricihart - ElectTimeline C// 1.             {
    y      tr    
               e}`);
${countryNamrts for dering cha(`📊 Renlog  console.         ) {
 me, coordsuntryNaCharts(coction renderfun

           }}
           ;
                `     div>
  </                  /div>
 ore<">Scitv class="un        <di                /div>
ss * 0.2)}<coords.acceund(60 + ${Math.roalue">"vdiv class=       <           
      ncy</h4>ciefi Ef <h4>Energy              
         ">metric-cards="lasdiv c    <           /div>
             <          v>
  di"unit">%</class= <div                      
  }</div>3)0.ess * + coords.acc20 nd(th.rou">${Mae"valus=iv clas      <d               
   h4>ial</entenewable Pot     <h4>R               d">
    car"metric-iv class=        <d    
             </div>       
        ">Mt</div>lass="unitiv c<d                  
      00)}</div> / 10oords.co2round(cath.alue">${Mclass="v       <div                s</h4>
  ₂ Emission   <h4>CO            
         d">carss="metric-   <div cla                  </div>
         
          /div>nit">%<"u=assdiv cl        <            /div>
    ess}<cc${coords.aalue">="vv class        <di          >
       Access</h4ty>Electrici  <h4                      ">
cardric-s="metv clas <di            
       L = `rHTMcCards.inne       metri{
         rds) Caif (metric   
         cCards');metri('IdntBymeument.getEleards = doctricCconst me           {
  ds)ame, coorntryNricCards(couMettion update       func  }

      );
 oordsName, countryharts(c   renderC   s
      chartr  Rende//            
      }
       
           ';lockdisplay = 'be.ion.stylSectesult        r     n) {
   Sectiosult  if (re         ion');
 ltSectesud('rElementByIument.getion = docultSect   const res         ion
 sectresultsShow      //           
   s);
      yName, coord(countrdsicCarMetr update   
        tric cards Update me    //
                 }
     
           Analysis`;me} - Energy${countryNat = `en.textContmentEleitle   t          
   ment) {tleEle if (ti          
 yTitle');yId('countrntBmet.getEle= document titleElemen     const       
  title/ Update      /                
turn;
  ords) ref (!co           iame];
 yNountrdinates[cooryC = countrrdsoot cons   c     {
    me) n(countryNaltsSection showResu     functio        }

     }
  ;
        ker = nullntMarurre     c         ker);
  (currentMaroveLayer     map.rem          {
  tMarker)  if (curren       
             }
  ull; = nghtLayerHighliurrent      c      er);
    htLayentHighlig(curroveLayerap.rem    m           Layer) {
 tHighlight  if (curren       s() {
   ighlighton clearMapHctifun

         }       );
   }        n: 1.5
      duratio        true,
    nimate:       a   , {
       5oords.lng],rds.lat, c.flyTo([coo  map          country
on Center map  // 
                     ;
   = markerrker  currentMa        ircle;
  htC highliger =ghtLayrrentHighli cu        
   rencesrefe// Store              
           );
nPopup(   .ope        `)
                        </div>
              /p>
   000)} Mt<ds.co2 / 1or(co{Math.round $strong></₂ Emissions:rong>CO><st     <p                  >
 cess}%</pds.ac${coor> ss:</strongcity Acceng>Electriro      <p><st                  e}</h5>
countryNam${        <h5>             ">
   x;: 10per; paddingnt ceign:"text-alle=sty<div                     (`
 .bindPopup           p)
    o(ma     .addT         s.lng])
   coordords.lat,er([co L.mark =kerconst mar         er
   markpin    // Add 
                 p);
    .addTo(ma     })   2
     eight:      w       00000,
   ius: 5   rad            6,
 : 0.city    fillOpa   
         E90',lor: '#90E     fillCo        
    '#32CD32',lor:         co{
       , ds.lng]at, coors.lle([coordirc L.cghtCircle =ghlionst hi       c
     ghtingill highliht green feate lig    // Cr      
          
    ghts();pHighlilearMa  c       
   tsighlighting har exis // Cle         
            ame}`);
  {countryNghting $🎯 Highliole.log(`  cons               
 ;
      rn !map) retus ||oord if (!c          ryName];
 tes[countdinantryCoors = courd  const coo
          ame) {ryNMap(counttCountryOnghn highliio funct   

    
        }y);foundCountrtion(sSechowResult  s   n
       lts sectio// Show resu                   
 ry);
    ndCount(fouMaptCountryOnghhighli      
      ap mtry onight coun    // Highl                
   untry}`);
 : ${foundCo countryog(`✅ Foundconsole.l  
          try;= foundCounntry  currentCou        }

     
          ry; foundCountut.value =tryInp       coun{
         ntryInput) if (cou           
 ntryInput');Id('couementBy.getElment= docuyInput tr  const coun    name
      ry ect countut with corrUpdate inp        // 

     }        turn;
          re        );
 t(message        aler     
                 
           }  `;
      etc.ance,Japan, FrChina, il, y, Braza, Germandior: Inng fry searchi\\n\\nTage += `   mess                  } else {
        ;
       \\n• ')}`'ons.join(• ${suggestise?\\nthee of onmean Did you \n= `\\n\e +essag       m       
       0) {ength >tions.luggesif (s             e.`;
   bas our datable inaila is not avme}"ountryNa "${c = `Sorry,essageet m           l    
        
         slice(0, 5);).               ))
 string(0, 3uberCase().sow.toLuntryName.includes(coe()aserCy.toLow        ke           => 
 r(key Keys.filte= countrysuggestions st con            ns
    e suggestiohow availabl  // S                   
           ;
 not found`)ame}"yNntrry "${couog(`❌ Countle.lonso        c
        try) {oundCoun   if (!f              }

     
     );          e())
   rCaswes(key.toLoudese().inclme.toLowerCatryNaun        co         
   )) ||ase(erC.toLowntryNameou.includes(cse()y.toLowerCa      ke           ey => 
   ys.find(kcountryKeCountry =    found       
      tial matchparry     // T         ) {
   undCountry     if (!fo       
      }
                    );
            erCase()
  ame.toLowyN) === countrwerCase(ey.toLo       k          
   find(key => ys.ntryKe coutry =dCoun    foun          tch
  ve mase-insensiti   // Try ca           {
    } else        me;
    countryNary =ountoundC    f  
          ) {Name]untry[coCoordinatesif (country        
    exact matchry // First t         
    
           dinates);untryCoorect.keys(co= Objys untryKenst co       co
     ull; = nfoundCountry    let       
  ive)itse-insens (ca in our dataexistscountry k if    // Chec
         }"`);
Name{country "$ing for:(`🔍 Searchogle.l      conso           }

       rn;
   retu            st!');
 y name fir countr select ar orPlease entealert('            ) {
    ountryName(!cf   i      
                );
ountry(electedC = getSNamet country cons        
   untry() {ctedCoyzeSele analunction    f   }

     });
          );
      ild(itempendChs.aptionesearchSugg      s         ountry);
 ch(cSearomtryFr selectCoun) =>ck = ( item.oncli              hite';
 ndColor = 'wroukg.bacle.sty> item() =ut = .onmouseo        item
        f9fa';or = '#f8roundColackgyle.bitem.st=>  = () ouseover.onmitem          
      ntry;tent = couitem.textCon              `;
                 or 0.2s;
 ckground-colition: ba      trans             0f0;
 d #f0fx soliom: 1p border-bott                  ;
 ntercursor: poi                 15px;
   ing: 12px add    p              
  ssText = `m.style.c   ite           );
  nt('div'mecreateEleent.= documconst item        
         try => {ound.forEach(c     filtere           
  ';
      'none:  'block' ngth > 0 ?iltered.ledisplay = fons.style.uggestihS  searc      
    rHTML = '';ns.innestioSugge   search
                
              );ery)
   qu().includes(werCasery.toLo       count   
       r(country =>ries.filteuntcod = re const filte                 
      
urn;etns) rgestio (!searchSug          if
  ions');gestearchSugmentById('sment.getElens = docuioestchSuggnst sear       co   
   {s(query)ountriefilterCon      functi
    }
        });
                   item);
d(dChiltions.appensearchSugges         
       try);(counromSearchuntryFelectCo) => snclick = (      item.o
          ite'; 'whdColor =ckgrountyle.ba() => item.suseout = onmo    item.       
     = '#f8f9fa';olor roundCyle.backgtem.st= () => inmouseover     item.o            ;
= countryextContent     item.t             `;
         s;
       0.2colorkground-tion: bac      transi          f0;
    lid #f0f0sopx ttom: 1border-bo           
         r: pointer;rso         cu         px;
  ng: 12px 15     paddi              = `
  le.cssTextstyitem.            );
    div'Element('ument.createem = doconst it         c     {
  untry => ).forEach(co, 20ries.slice(0      count
               ock';
    'bly =latyle.disps.shSuggestionrc     sea       = '';
innerHTML ons.estichSugg    sear             
   rn;
    etus) rtionesrchSugg    if (!sea        stions');
searchSuggentById('lemegetEument.= docestions uggrchS  const sea      () {
    untriesCohowAllfunction s
                  }
            });

                }';
       = 'nonesplayons.style.distirchSugge sea                  rget)) {
 s(e.ta.containhSuggestions  !searc           
        && et)(e.targut.containsnpuntryI    !co             ns && 
   gestiosearchSugf (   i            e) {
 unction(k', ftener('clicventLisument.addEdoc            utside
clicking ostions when uggede s   // Hi 
              });
           
           }            }`);
ntryectedCouel ${som dropdown:selected fr🔽 Country e.log(`onsol  c                e';
   'none.display =yltions.sthSuggesrcns) seaioSuggest (search         if          untry;
 tedCo selecut.value =tryInp      coun           ry) {
   Countected (sel   if        
     e;his.valudCountry = tselecte     const            nction() {
ange', fur('chenentListdEverySelect.adunt    co  
      nctionality change fuopdownDr/       /
             );
           }  
             }   ();
    ieswAllCountrsho         
           th === 0) {s.value.leng(thi if        {
        ction() ocus', funer('ftListendEven.adnputntryI  cou
          on inputcking cliies when  countr// Show all               
   
        });     }
                 = '';
    lect.value ySe      countr          
    es(query);tri  filterCoun                else {
          }     '';
     e =t.valutrySelec     coun         
      none';display = 'e.styluggestions.s) searchSstion(searchSuggef   i                  {
 gth === 0)len(query.  if     
          erCase();.toLowalue this.vry =const que              on() {
  tiuncinput', f('enerListddEventuntryInput.a       colity
     nctionanput fuch i// Sear          
             turn;
 Select) reountry| !cyInput |ountrf (!c  i            
  );
        Suggestions'yId('searchtElementB.gedocumentggestions = searchSu  const           Select');
ountrytById('cnt.getElemenect = documeySelconst countr  
          t');puInuntrymentById('cont.getEle documet =Inpu country       const {
     onality()archFunction setupSefuncti

             }      }
;
         ed:', error)on failnitializatiror('❌ Map isole.er     con          error) {
 atch (    } c           
             lly');
ed successfuinitializ Map og('✅ console.l             
         
         dTo(map);     }).ad      18
      maxZoom:         
           tors',ontributMap cStree© Openbution: 'riatt                    png', {
}/{y}./{xz}etmap.org/{tre.tile.openstps://{s}htLayer('L.tile              
                2);
   0],View([20, ('map').set.mapmap = L          {
      y         tr          
 
     ..');p.ng maliziitia🗺️ Ing('.lole    conso    
    izeMap() {itialn in    functio

          });
  fully!'); successtializedrd ini('✅ Dashboale.logconso         down();
   ropyDCountrpopulate            y();
ctionalitearchFunetupS s        ;
   alizeMap()     initi
       ard...');Dashbozing ('🚀 Initiali.log     console       {
 function() ntLoaded',teDOMConListener('ntveaddE document.   ion
    plicate aplize th// Initia     
   sort();
s).tenaCoordis(countryt.keyies = Objecountr c       constst
 ountries lible claai/ Av
        /;
    }00 }
     2820o2: cs: 99.0,2772, acces lng: 108.at: 14.0583,m': { ltnaVie           '56000 },
 0, co2: 1ss: 99.acce-66.5897,  lng: t: 6.4238,la': { lanezue   'Ve          114000 },
100.0, co2: access: 5853,g: 64. ln5,: 41.377stan': { latbeki      'Uz
      0 },7009.7, co2: cess: 95.7658, ac lng: -5.5228,-32y': { lat:      'Urugua     ,
  2: 5416000 }cos: 100.0, 5, acceslng: -98.579, 283at: 39.8': { ld States    'Unite    ,
    : 351000 } co200.0,ess: 160, acc.4381, lng: -337t: 55.: { lagdom'nited Kin        'U  0000 },
  202: 0.0, co access: 103.8478, lng: 54241,t: 23.lamirates': { ed Arab E      'Unit
      00 },200.0, co2: 20ess: 101.1656, acclng: 33794,  lat: 48.': {   'Ukraine
         0 },: 35300100.0, co2s: 2433, acces lng: 35.9637,38. lat: rkey': {'Tu          000 },
  9.9, co2: 435, access: 9 -61.22218, lng: lat: 10.69d Tobago': {d anidaTrin      '
      73000 },2: 2s: 99.8, co.9925, acces100.8700, lng: { lat: 15and': il       'Tha
     000 },0, co2: 38100.5, access: 8.227182, lng:  46.8t:land': { la   'Switzer       000 },
  0.0, co2: 35ess: 108.6435, acclng: 1t: 60.1282, : { la  'Sweden'        0 },
  o2: 2300100.0, cccess: 0.7718, ang: 88731, l: { lat: 7.ka'  'Sri Lan        58000 },
  co2: 2100.0, 92, access:  lng: -3.744637,: 40.at': { lin     'Spa    000 },
    co2: 611 100.0,ess:acc: 127.7669, ng.9078, lt: 35la': { orea    'South K     ,
   56000 }2, co2: 484.: ess5, acc937: 22. lng0.5595,: { lat: -3 Africa'     'South    000 },
   , co2: 14s: 100.0cces.9955, a, lng: 14 46.1512 { lat:':niaove       'Sl      },
, co2: 32000: 100.0ess, accg: 19.69908.6690, lnt: 4vakia': { la'Slo            
0 },700 3.0, co2:: 10098, access03.81lng: 1521, : { lat: 1.3ngapore'  'Si
          1000 },0.0, co2: ess: 10, accg: 55.4920796, lnat: -4.6lles': { l   'Seyche
         2: 50000 },.0, co00access: 1059,  21.05, lng:164.0: { lat: 4a'      'Serbi0 },
      : 51700.0, co2100access: g: 45.0792,  ln3.8859, 2{ lat:': udi ArabiaSa       '
     000 }, 17110.0, co2:access: 10 105.3188,  lng:1.5240,at: 6sia': { lus    'R  
      69000 },o2: s: 100.0, c.9668, acces, lng: 24at: 45.9432nia': { lRoma  '           103000 },
00.0, co2:ccess: 11839, ag: 51.ln,  25.3548at:'Qatar': { l         ,
   00 }: 480: 100.0, co2ess.2245, acc lng: -8 39.3999,l': { lat:tuga        'Por   0 },
 41000.0, co2: 3ccess: 1019.1451, a94, lng: at: 51.91': { l 'Poland           },
 2: 122000s: 94.8, co740, acces lng: 121.7 12.8797,': { lat:ppineshili 'P     },
      00  co2: 570ss: 95.5,2, acce15.00, lng: -75 lat: -9.190eru': {   'P       },
   7000.7, co2: , access: 994438ng: -58.5, lt: -23.442 laaguay': {'Par     ,
       2: 11000 } 91.8, co1, access:0.78280, lng: -8lat: 8.53': {  'Panama          01000 },
 73.1, co2: 2ss: cce a69.3451,3, lng: .375: { lat: 30tan'    'Pakis    
    }, 68000 100.0, co2:, access: 97545, lng: 55.73 lat: 21.4': {an         'Om  5000 },
 co2: 300.0, cess: 1ac.4689, 720, lng: 8lat: 60.4': {  'Norway        000 },
   0, co2: 2826.ess: , acc: 127.510140.3399, lng: { lat: h Korea' 'Nort           04000 },
co2: 1, s: 62.0ces.6753, acg: 8: 9.0820, lna': { latNigeri '           0 },
0, co2: 3700s: 100.60, accesg: 174.88-40.9006, ln: { lat: aland'Ze 'New            
: 162000 },co200.0, ss: 1cce2913, a, lng: 5.2.1326{ lat: 5herlands':      'Net       : 3000 },
, co2.7cess: 9040, ac.12 843949, lng:28.{ lat: 'Nepal':     },
        co2: 21000 ss: 70.1, acce, ng: 95.9560 21.9162, lat:mar': { l'Myan           00 },
 610, co2: 9.4cess: 9 -7.0926, acng:1.7917, l{ lat: 3: occo'        'Mor
    0 }, co2: 2400ss: 90.0,, acceg: 106.9057, lnlat: 47.0105ia': {      'Mongol     6000 },
  48 99.4, co2: , access:102.5528 lng: -6345,23.t: exico': { la         'M0 },
    co2: 5000,00.s: 1accesg: 57.5522, 84, ln34: -20. { latius': 'Maurit           : 2000 },
100.0, co2cess: ac4,  14.375375, lng: { lat: 35.9  'Malta':
          ,00 }: 20co2ess: 100.0, 7, acclng: 73.220028, .2': { lat: 3ldives    'Ma       
 4000 },, co2: 25access: 99.858, .97 lng: 10105,.21: 4 { lat 'Malaysia':     ,
      000 }co2: 10.0, ss: 100 acce296, 6.1, lng:at: 49.8153urg': { luxembo 'L        0 },
   2: 1400, coess: 100.0 acc3.8813,1694, lng: 255. { lat: ':uania 'Lith          2000 },
 0.0, co2: 2ccess: 10: 35.8623, a3.8547, lng{ lat: 3ebanon':          'L
   2: 7000 },100.0, co: access4.6032,  28796, lng: 56.': { lat: 'Latvia           ,
000 }co2: 17, 95.0cess: 5, acg: 102.49563, ln: 19.85 { lat':     'Laos      000 },
 0.0, co2: 92ccess: 1047.4818, a7, lng:  29.311{ lat:'Kuwait':            },
   co2: 17000ess: 71.4,7.9062, acc lng: 36,t: -0.023ya': { la      'Ken
       267000 },co2:ss: 100.0, 237, acce lng: 66.948.0196,at: hstan': { lak       'Kaz0 },
      co2: 230000.0,ess: 184, accng: 36.2352, l lat: 30.58n': {     'Jorda},
        1162000  co2:s: 100.0,acces529, 8.2 13ng: 36.2048, ln': { lat:     'Japa       },
000  co2: 98.8, 9975, access:lng: -77.2: 18.1096, lat: {   'Jamaica'
           }, 3350002: 100.0, coaccess: 12.5674,  lng:19, 41.87t:': { la  'Italy        
  5000 }, co2: 6: 100.0,ccess a34.8516,61, lng:  lat: 31.04'Israel': {   
         000 },, co2: 37 100.039, access:.249, lng: -8at: 53.412{ lreland':  'I        
   90000 },: 1100.0, co2access: 793,  43.6 lng: 33.2232,t:: { laaq'Ir           '2000 },
  67 100.0, co2:0, access:53.688 lng: t: 32.4279,: { la     'Iran'   0 },
     61500 97.8, co2:3, access:13.921 1, lng:at: -0.7893onesia': { l   'Ind       
  : 2654000 },95.2, co2access: : 78.9629, 7, lng 20.593ia': { lat:nd        'I0 },
    , co2: 200cess: 100.0, ac19.0208 lng: -64.9631, lat: : {  'Iceland'     0 },
     o2: 4800ss: 100.0, c.5033, acce5, lng: 19t: 47.162ary': { laung'H            67000 },
 .0, co2:00 access: 1.8243,742, lng: 21at: 39.0: { l 'Greece'        000 },
    162: cos: 85.0,ces ac-1.0232,g:  7.9465, ln{ lat:'Ghana':          ,
    729000 }00.0, co2:ccess: 1 ang: 10.4515,1.1657, l: 5ny': { latGerma '       000 },
    2: 100, cocess: 100.3569, ac4, lng: 43.42.315{ lat: orgia':         'Ge},
    00 0, co2: 3300100.ss: 8883, accelng: 1.: 46.6034, ': { latrance  'F
          5000 }, 4100.0, co2: access: 5.7482, 2241, lng:.9{ lat: 61land': Fin        ',
    co2: 14000 }: 44.3, cess97, ac 40.481450, lng: { lat: 9.thiopia':         'E00 },
    160o2:s: 100.0, c.0136, acces53, lng: 25at: 58.59{ la': nito        'Es
    2: 234000 },6, co 99.5, access:30.8026, lng: lat: 26.820 {  'Egypt':       },
    0 , co2: 3800access: 97.21834,  lng: -78..8312,at: -1r': { luado 'Ec          },
  , co2: 22000: 98.1ess627, acclng: -70.157,  18.73 { lat:c':can Republiini       'Dom0 },
      co2: 310000.0,ccess: 1g: 9.5018, a, ln6.2639': { lat: 5rk   'Denma    
     00 }, 1070.0, co2:00 1ess:acc, 30.47g: 15 ln75,819.t: 4: { la Republic'ech    'Cz
        },2: 7000 0, co: 100.4299, access33.g: 5.1264, ln{ lat: 3rus': Cyp      ',
      000 } 26o2:00.0, c, access: 1ng: -77.7812 21.5218, lt: la': {uba    'C},
        0 2: 18000, coccess: 100.0, a: 15.200000, lng45.1{ lat: ia':  'Croat          8000 },
 o2: .7, c, access: 99.7534: -83.7489, lng { lat: 9sta Rica':   'Co        4000 },
 co2: 897.4, 3, access: g: -74.2979, ln70 { lat: 4.5ombia':   'Col      00 },
   50 co2: 1006: 100.0,cess ac4.1954,617, lng: 10 { lat: 35.8 'China':         ,
  00 }8, co2: 870 access: 99.5430,, lng: -71..6751t: -35Chile': { la   '
         672000 },0, co2: 00.s: 1 acces8,06.346-1, lng: 56.1304: ada': { lat  'Can
          00 },100, co2: s: 89.1es, acc 104.99107, lng: 12.565': { lat:odia     'Camb       1000 },
00.0, co2: 4 access: 1858,, lng: 25.4392.73': { lat: 4 'Bulgaria       ,
     }100000, co2: ss: 100., acce114.7277ng: 4.5353, l: ': { lat'Brunei       ,
     2000 }o2: 4699.7, ccess: 1.9253, aclng: -5-14.2350, l': { lat:     'Brazi       ,
 00 }, co2: 250100.0ss:  acce: 17.6791,59, lng: 43.91ina': { latd Herzegovosnia an'B           
 000 },, co2: 21ss: 93.0ce, ac: -63.5887, lng022916. lat: -: {ia'     'Boliv       ,
2000 }100.0, co2: 36, access: 0.43, lng: 9lat: 27.5142Bhutan': {            '14000 },
 , co2: 1s: 100.0 acces 4.4699,5039, lng:0.m': { lat: 5iuelg 'B          
 000 },0, co2: 58ccess: 100.34, alng: 27.95098, .7at: 53us': { l   'Belar
          84000 },2, co2: access: 92.0.3563,6850, lng: 9 23.lat: { gladesh':      'Ban
      2: 23000 },, co0.0, access: 10g: 50.6378, ln: 25.9304: { latrain' 'Bah        
   ,7000 }0, co2: 3access: 100.47.5769, 431, lng: lat: 40.1: { jan' 'Azerbai
            }, 720000.0, co2: access: 10g: 14.5501, 47.5162, ln lat:tria': {  'Aus         
 415000 },0.0, co2:  access: 10: 133.7751, lngt: -25.2744,ia': { laustral  'A   },
        co2: 5200  100.0,ess:cc2, ag: 45.038 ln 40.0691,lat:Armenia': {          '   1000 },
2, co2: 2099.cess: -63.6167, ac.4161, lng: lat: -38{ tina':      'Argen,
       0000 }co2: 159.4,  access: 91.6596,339, lng:  28.0{ lat:: geria' 'Al      },
      4500 , co2: 100.0access:20.1683, , lng: .1533 { lat: 41':  'Albania  ,
        00 }.7, co2: 90: 97cess67.7100, ac1, lng:  33.939 { lat:istan':  'Afghan   = {
       s nateryCoordist counton  cta
      h dadinates witountry coor C      //

  = null;ker  currentMar    letll;
    htLayer = nuhligntHig   let curre   null;
  ountry = et currentC     l   map;
 et l>
       pt  <scrit>
  "></scripeaflet.js4/dist/lflet@1.9./lea/unpkg.comhttps:/="<script src   iv>

     </ddiv>
      </>
  diveChart"></id="pi" -containerss="chartla      <div c
      ></div>art"ableChrenewner" id="ntai="chart-co class        <div</div>
    essChart">id="accntainer" "chart-colass= <div c         
  >"></divart"mainChner" id=rt-contai