//柱状图 左一
(function () {
  //1、实例化对象
  var myChart = echarts.init(document.querySelector(".bar .chart"));
  //2、指定配置项和数据
  var option = {
    tooltip: {
      trigger: "axis",
      axisPointer: {
        type: "shadow",
      },
    },
    grid: {
      left: "3%",
      right: "4%",
      bottom: "1%",
      top: "6%",
      containLabel: true,
    },
    xAxis: [
      {
        type: "category",
        data: ["大沙", "簰洲", "金口", "武汉", "阳逻", "黄冈", "黄石", "蕲州"],
        axisTick: {
          alignWithLabel: true,
        },
      },
    ],
    yAxis: [
      {
        type: "value",
      },
    ],
    series: [
      {
        name: "Direct",
        type: "bar",
        barWidth: "60%",
        data: [90, 70, 60, 50, 40, 30, 20, 20],
      },
    ],
  };
  myChart.setOption(option);

  $(document).ready(function () {
    $.getJSON("/get_data", function (data) {
      //console.log(data); // 在控制台中打印接收到的数据
      sjzl = data[8];
      myChart.setOption({ series: [{ data: sjzl }] });
      // 你可以在这里根据data执行更多的JavaScript代码
    });
  });
  //让图表自适应
  window.addEventListener("resize", function () {
    myChart.resize();
  });
})();
//左二
(function () {
  var myChart = echarts.init(document.querySelector(".line .chart"));
  var option = {
    legend: {},
    tooltip: {},
    dataset: {
      source: [
        ["水位站数据", "完整率", "准确率"],
        ["莫家河", 43.3, 85.8],
        ["簰洲", 83.1, 73.4],
        ["军山", 86.4, 65.2],
        ["汉口", 72.4, 53.9],
        ["阳逻", 72.4, 53.9],
        ["鄂州", 72.4, 53.9],
        ["黄石", 72.4, 53.9],
        ["蕲春", 72.4, 53.9],
      ],
    },
    grid: {
      left: "9%",
      right: "3%",
      bottom: "13%",
      top: "18%",
      // containLabel: true
    },
    xAxis: { type: "category" },
    yAxis: {},
    // Declare several bar series, each will be mapped
    // to a column of dataset.source by default.
    series: [{ type: "bar" }, { type: "bar" }],
  };
  myChart.setOption(option);

  $(document).ready(function () {
    $.getJSON("/get_data", function (data) {
      swzzd = data[9];
      //console.log(data); // 在控制台中打印接收到的数据
      console.log(swzzd);
      myChart.setOption({ dataset: [{ source: swzzd }] });
      // 你可以在这里根据data执行更多的JavaScript代码
    });
  });

  window.addEventListener("resize", function () {
    myChart.resize();
  });
})();
//柱状图 左三
(function () {
  //1、实例化对象
  var myChart = echarts.init(document.querySelector(".pie .chart"));
  //2、指定配置项和数据
  var option = {
    tooltip: {
      trigger: "axis",
      axisPointer: {
        type: "cross",
        crossStyle: {
          color: "#999",
        },
      },
    },
    grid: {
      left: "9%",
      right: "11%",
      bottom: "13%",
      top: "18%",
      // containLabel: true
    },
    xAxis: [
      {
        type: "category",
        data: ["大沙", "簰洲", "金口", "武汉", "阳逻", "黄冈", "黄石", "蕲州"],
        axisPointer: {
          type: "shadow",
        },
      },
    ],
    yAxis: [
      {
        type: "value",
        name: "索赔率(%)",
        min: 0,
        max: 100,
        interval: 20,
        // axisLabel: {
        //    formatter: '{value} %'
        // }
      },
      {
        type: "value",
        name: "索赔金额(万)",
        min: 0,
        max: 50,
        interval: 10,
        // axisLabel: {
        //   formatter: '{value} 万'
        // }
      },
    ],
    series: [
      {
        name: "索赔率",
        type: "bar",
        data: [10, 20, 30, 40, 50, 60, 70, 80],
      },
      {
        name: "索赔金额",
        type: "bar",
        // tooltip: {
        //   valueFormatter: function (value) {
        //     return value + ' ml';
        //   }
        // },
        data: [10, 20, 30, 40, 50, 60, 70, 80],
      },
    ],
  };
  myChart.setOption(option);

  $(document).ready(function () {
    $.getJSON("/get_data", function (data) {
      //console.log(data); // 在控制台中打印接收到的数据
      console.log(data);
      spl = data[0][0];
      spje = data[1][0];
      myChart.setOption({ series: [{ data: spl }, { data: spje }] });
      // 你可以在这里根据data执行更多的JavaScript代码
    });
  });
  window.addEventListener("resize", function () {
    myChart.resize();
  });
})();
//---------------------------测绘内业开始-----------------------------------
//@倪忻亮
//@date:2024.8.11
(function () {
        let ch_data=[];
        let f_excellent_data;
        let f_good_data;
        let f_average_data;
        let f_poor_data;
        // 1实例化对象
        var myChart = echarts.init(document.querySelector(".bar2 .chart"));
        // 2. 指定配置项和数据
        var option = {
          tooltip: {
            trigger: "axis",
            axisPointer: {
              // Use axis to trigger tooltip
              type: "shadow", // 'shadow' as default; can also be 'line' or 'shadow'
            },
          },
          //麻痹的这个是类别
          legend: {
            date: ["优", "良", "中", "差"],
            textStyle: {
              color: "rgba(255,255,255,.6)",
            },
          },
          grid: {
            left: "0%",
            right: "0%",
            bottom: "3%",
            containLabel: true,
          },
          textStyle: {
            color: "rgba(255,255,255,.6)",
            fontSize: "15",
          },
          xAxis: {
            type: "category",
            axisLabel: {
            fontSize: 12 //设置坐标轴文本标签的字体大小
             },
            data: [
              "大沙",
              "簰洲",
              "金口",
              "武汉",
              "阳逻",
              "黄冈",
              "黄石",
              "蕲州",
              "武测",
              "黄测",
            ],
          },
          yAxis: {
            type: "value",
          },
          series: [
            {
              name: "优",
              type: "bar",
              stack: "total",
              label: {
                show: true,
              },
              emphasis: {
                focus: "series",
              },
              data: f_excellent_data,
            },
            {
              name: "良",
              type: "bar",
              stack: "total",
              label: {
                show: true,
              },
              emphasis: {
                label: {
                  color: "rgba(255,255,255,.6)",
                },
                focus: "series",
              },
              data: f_good_data,
            },
            {
              name: "中",
              type: "bar",
              stack: "total",
              label: {
                show: true,
              },
              emphasis: {
                focus: "series",
              },
              data: f_average_data
            },
            {
              name: "差",
              type: "bar",
              stack: "total",
              label: {
                show: true,
              },
              emphasis: {
                focus: "series",
              },
              data: f_poor_data
            },
          ],
        };
        // 3. 把配置项给实例对象
        myChart.setOption(option);

        $(document).ready(function () {
          $.getJSON("/get_data", function (data) {
            console.log(data); // 在控制台中打印接收到的数据
            ch_data=data[11];
            f_excellent_data = ch_data[1][0];
            f_good_data = ch_data[1][1];
            f_average_data = ch_data[1][2];
            f_poor_data = ch_data[1][3];
            console.log(f_poor_data);

            myChart.setOption({ series: [{ data: f_excellent_data }, { data: f_good_data },{data: f_average_data},{data: f_poor_data}] });
          // 你可以在这里根据data执行更多的JavaScript代码
          });
        });
        // 4. 让图表跟随屏幕自动的去适应
        window.addEventListener("resize", function () {
          myChart.resize();
        });
      })();
//------------------------------测绘内业结束---------------------------------------

//----------------------------测绘外业开始-----------------------------------------
//@倪忻亮
//@date：2024.8.11
(function () {
        let ch_data=[];
        let i_excellent_data;
        let i_good_data;
        let i_average_data;
        let i_poor_data;
        // 1实例化对象
        var myChart = echarts.init(document.querySelector(".bar3 .chart"));
        // 2. 指定配置项和数据
        var option = {
          tooltip: {
            trigger: "axis",
            axisPointer: {
              // Use axis to trigger tooltip
              type: "shadow", // 'shadow' as default; can also be 'line' or 'shadow'
            },
          },
          //麻痹的这个是类别
          legend: {
            date: ["优", "良", "中", "差"],
            textStyle: {
              color: "rgba(255,255,255,.6)",
            },
          },
          grid: {
            left: "0%",
            right: "0%",
            bottom: "3%",
            containLabel: true,
          },
          textStyle: {
            color: "rgba(255,255,255,.6)",
            fontSize: "15",
          },
          xAxis: {
            type: "category",
            axisLabel: {
            fontSize: 12 //设置坐标轴文本标签的字体大小
             },
            data: [
              "大沙",
              "簰洲",
              "金口",
              "武汉",
              "阳逻",
              "黄冈",
              "黄石",
              "蕲州",
              "武测",
              "黄测",
            ],
          },
          yAxis: {
            type: "value",
          },
          series: [
            {
              name: "优",
              type: "bar",
              stack: "total",
              label: {
                show: true,
              },
              emphasis: {
                focus: "series",
              },
              data: i_excellent_data,
            },
            {
              name: "良",
              type: "bar",
              stack: "total",
              label: {
                show: true,
              },
              emphasis: {
                label: {
                  color: "rgba(255,255,255,.6)",
                },
                focus: "series",
              },
              data: i_good_data,
            },
            {
              name: "中",
              type: "bar",
              stack: "total",
              label: {
                show: true,
              },
              emphasis: {
                focus: "series",
              },
              data: i_average_data
            },
            {
              name: "差",
              type: "bar",
              stack: "total",
              label: {
                show: true,
              },
              emphasis: {
                focus: "series",
              },
              data: i_poor_data
            },
          ],
        };
        // 3. 把配置项给实例对象
        myChart.setOption(option);

        $(document).ready(function () {
          $.getJSON("/get_data", function (data) {
            console.log(data); // 在控制台中打印接收到的数据
            ch_data=data[11];
            i_excellent_data = ch_data[0][0];
            i_good_data = ch_data[0][1];
            i_average_data = ch_data[0][2];
            i_poor_data = ch_data[0][3];
            console.log(i_poor_data);

            myChart.setOption({ series: [{ data: i_excellent_data }, { data: i_good_data },{data: i_average_data},{data: i_poor_data}] });
          // 你可以在这里根据data执行更多的JavaScript代码
          });
        });
        // 4. 让图表跟随屏幕自动的去适应
        window.addEventListener("resize", function () {
          myChart.resize();
        });
      })();
//------------------------------测绘外业结束--------------------------------------


//中一
(function () {
  var myChart = echarts.init(document.querySelector(".bar0 .chart"));
  var option = {
    grid: {
      left: "3%",
      right: "4%",
      bottom: "1%",
      top: "6%",
      containLabel: true,
    },
    xAxis: {
      type: "category",
      data: ["大沙", "簰洲", "金口", "武汉", "阳逻", "黄冈", "黄石", "蕲州"],
    },
    yAxis: {
      type: "value",
    },
    series: [
      {
        data: [
          100,
          {
            value: 100,
            //            itemStyle: {
            //              color: '#a90000'
            //            }
          },
          100,
          100,
          100,
          100,
          100,
          100,
        ],
        type: "bar",
      },
    ],
  };
  myChart.setOption(option);
  window.addEventListener("resize", function () {
    myChart.resize();
  });
})();

// //中二
// (function () {
//   var myChart = echarts.init(document.querySelector(".line0 .chart"));
//   var option = {
//     tooltip: {
//       trigger: "axis",
//       axisPointer: {
//         type: "shadow",
//       },
//     },
//     grid: {
//       left: "3%",
//       right: "4%",
//       bottom: "3%",
//       top: "3%",
//       containLabel: true,
//     },
//     xAxis: {
//       type: "value",
//       boundaryGap: [0, 0.01],
//     },
//     yAxis: {
//       type: "category",
//       data: ["蕲州", "黄石", "黄冈", "阳逻", "武汉", "金口", "簰洲", "大沙"],
//     },
//     series: [
//       {
//         name: "2011",
//         type: "bar",
//         data: [90, 60, 90, 70, 90, 90, 80, 90],
//       },
//     ],
//   };
//   myChart.setOption(option);
//   $(document).ready(function () {
//     $.getJSON("/get_data", function (data) {
//       //console.log(data); // 在控制台中打印接收到的数据
//       hbschf = data[10];
//       myChart.setOption({ series: [{ data: hbschf }] });
//       // 你可以在这里根据data执行更多的JavaScript代码
//     });
//   });
//   window.addEventListener("resize", function () {
//     myChart.resize();
//   });
// })();
//
// //中三
// (function () {
//   var myChart = echarts.init(document.querySelector(".pie0 .chart"));
//   const rawData = [
//     [100, 302, 301, 334, 390, 330, 320, 320],
//     [320, 132, 101, 134, 90, 230, 210, 320],
//     [220, 182, 191, 234, 290, 330, 310, 320],
//     [150, 212, 201, 154, 190, 330, 410, 320],
//     [820, 832, 901, 934, 1290, 1330, 1320, 320],
//   ];
//   const totalData = [];
//   for (let i = 0; i < rawData[0].length; ++i) {
//     let sum = 0;
//     for (let j = 0; j < rawData.length; ++j) {
//       sum += rawData[j][i];
//     }
//     totalData.push(sum);
//   }
//   const grid = {
//     left: 100,
//     right: 100,
//     top: 50,
//     bottom: 50,
//   };
//   const series = [
//     "Direct",
//     "Mail Ad",
//     "Affiliate Ad",
//     "Video Ad",
//     "Search Engine",
//   ].map((name, sid) => {
//     return {
//       name,
//       type: "bar",
//       stack: "total",
//       barWidth: "60%",
//       label: {
//         show: true,
//         formatter: (params) => Math.round(params.value * 1000) / 10 + "%",
//       },
//       data: rawData[sid].map((d, did) =>
//         totalData[did] <= 0 ? 0 : d / totalData[did]
//       ),
//     };
//   });
//   var option = {
//     legend: {
//       selectedMode: false,
//     },
//     grid: {
//       left: "5%",
//       right: "3%",
//       bottom: "12%",
//       top: "15%",
//       // containLabel: true
//     },
//     yAxis: {
//       type: "value",
//     },
//     xAxis: {
//       type: "category",
//       data: ["大沙", "簰洲", "金口", "武汉", "阳逻", "黄冈", "黄石", "蕲州"],
//     },
//     series,
//   };
//   myChart.setOption(option);
//   window.addEventListener("resize", function () {
//     myChart.resize();
//   });
// })();

//右一 折线图
var qxhb, yqxhb;
(function () {
  //1、实例化对象
  var myChart = echarts.init(document.querySelector(".bar1 .chart"));
  //2、指定配置项和数据
  var option = {
    grid: {
      left: "10%",
      right: "3%",
      bottom: "12%",
      top: "9%",
      // containLabel: true
    },
    tooltip: {
      trigger: "axis",
    },
    xAxis: {
      type: "category",
      data: ["大沙", "簰洲", "金口", "武汉", "阳逻", "黄冈", "黄石", "蕲州"],
    },
    yAxis: {
      type: "value",
    },
    series: [
      {
        name: "浮标在用数",
        data: [150, 230, 224, 218, 135, 147, 260, 260],
        //data:qxhb,
        type: "line",
      },
      {
        name: "已清洗数量",
        data: [50, 30, 24, 18, 35, 47, 60, 60],
        //data:yqxhb,
        type: "line",
      },
    ],
  };
  myChart.setOption(option);

  $(document).ready(function () {
    $.getJSON("/get_data", function (data) {
      //console.log(data); // 在控制台中打印接收到的数据
      qxhb = data[4][0];
      yqxhb = data[5][0];
      myChart.setOption({ series: [{ data: qxhb }, { data: yqxhb }] });
      // 你可以在这里根据data执行更多的JavaScript代码
    });
  });
  window.addEventListener("resize", function () {
    myChart.resize();
  });
})();
//右二
var tccd, ybcd;
(function () {
  //1、实例化对象
  var myChart = echarts.init(document.querySelector(".line1 .chart"));
  //2、指定配置项和数据
  var option = {
    tooltip: {
      trigger: "axis",
      axisPointer: {
        type: "cross",
        label: {
          backgroundColor: "#6a7985",
        },
      },
    },
    grid: {
      left: "3%",
      right: "4%",
      bottom: "3%",
      top: "8",
      containLabel: true,
    },
    xAxis: [
      {
        type: "category",
        boundaryGap: false,
        data: ["大沙", "簰洲", "金口", "武汉", "阳逻", "黄冈", "黄石", "蕲州"],
      },
    ],
    yAxis: [
      {
        type: "value",
      },
    ],
    series: [
      {
        name: "实测最小尺度",
        type: "line",
        //stack: 'Total',
        areaStyle: {},
        emphasis: {
          focus: "series",
        },
        //data: [120, 132, 101, 134, 90, 230, 210, 132]
        data: tccd,
      },
      {
        name: "周预报尺度",
        type: "line",
        stack: "Total",
        label: {
          show: true,
          position: "top",
        },
        areaStyle: {},
        emphasis: {
          focus: "series",
        },
        //data: [820, 932, 901, 934, 1290, 1330, 1320, 132]
        data: ybcd,
      },
    ],
  };
  myChart.setOption(option);

  $(document).ready(function () {
    $.getJSON("/get_data", function (data) {
      //console.log(data); // 在控制台中打印接收到的数据
      tccd = data[2][0];
      ybcd = data[3][0];
      //console.log(tccd)
      //console.log(ybcd)
      myChart.setOption({ series: [{ data: tccd }, { data: ybcd }] });
      // 你可以在这里根据data执行更多的JavaScript代码
    });
  });

  window.addEventListener("resize", function () {
    myChart.resize();
  });
})();

//  $.ajax({
//    type:'Get',
//    url:'/index.html',
//    async:true,
//    //dataType:'json',
//    success:function(data){
//       $.getJSON('/get_data', function(data) {
//                console.log(data); // 在控制台中打印接收到的数据
//                // 你可以在这里根据data执行更多的JavaScript代码
//            });
//       //console.log("123123")
//       //console.info(data);
//       //myChart.setOption({series:[data:ybcd]});
//    }
//  });
//右三
(function () {
  //1、实例化对象
  var myChart = echarts.init(document.querySelector(".pie1 .chart"));
  //2、指定配置项和数据
  var option = (option = {
    grid: {
      left: "1%",
      right: "2%",
      bottom: "3%",
      top: "8%",
      containLabel: true,
    },
    tooltip: {
      trigger: "axis",
    },
    xAxis: [
      {
        type: "category",
        data: ["索具", "锚具", "灯器", "标体", "浮具"],
        axisPointer: {
          type: "shadow",
        },
      },
    ],
    yAxis: [
      {
        type: "value",
        name: "备品率",
        min: 0,
        max: 500,
        interval: 80,
        // axisLabel: {
        //   formatter: '{value} ml'
        // }
      },
      {
        type: "value",
        name: "指标",
        min: 0,
        max: 500,
        interval: 80,
        // axisLabel: {
        //   formatter: '{value} °C'
        // }
      },
    ],
    series: [
      {
        name: "备品率",
        type: "bar",
        // tooltip: {
        //   valueFormatter: function (value) {
        //     return value + ' ml';
        //   }
        // },
        data: [26, 59, 90, 26, 28],
      },
      {
        name: "控制指标",
        type: "line",
        yAxisIndex: 1,
        // tooltip: {
        //   valueFormatter: function (value) {
        //     return value + ' °C';
        //   }
        // },
        data: [18, 22, 12, 15, 23],
      },
    ],
  });
  myChart.setOption(option);

  $(document).ready(function () {
    $.getJSON("/get_data", function (data) {
      //console.log(data); // 在控制台中打印接收到的数据bzbp,sjbp
      bzbp = data[6][0];
      sjbp = data[7][0];
      myChart.setOption({ series: [{ data: sjbp }, { data: bzbp }] });
      // 你可以在这里根据data执行更多的JavaScript代码
    });
  });

  window.addEventListener("resize", function () {
    myChart.resize();
  });
})();
//测绘
