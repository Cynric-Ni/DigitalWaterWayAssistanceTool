/*
 Navicat Premium Data Transfer

 Source Server         : nas_sql
 Source Server Type    : MySQL
 Source Server Version : 50743
 Source Host           : 10.10.10.4:3306
 Source Schema         : 检查结果

 Target Server Type    : MySQL
 Target Server Version : 50743
 File Encoding         : 65001

 Date: 06/05/2024 08:40:00
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for 失常综合分析
-- ----------------------------
DROP TABLE IF EXISTS `失常综合分析`;
CREATE TABLE `失常综合分析`  (
  `失常ID` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `单位` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `hb_id` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `航标` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `失常时间` datetime NULL DEFAULT NULL,
  `失常合并` datetime NULL DEFAULT NULL,
  `恢复时间` datetime NULL DEFAULT NULL,
  `失常类型合并` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `恢复时长` float NULL DEFAULT NULL,
  `失常恢复时限` int(11) NULL DEFAULT NULL,
  `报警ID` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `报警类型` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `报警开始时间` datetime NULL DEFAULT NULL,
  `报警结束时间` datetime NULL DEFAULT NULL,
  `最后调度时间` datetime NULL DEFAULT NULL,
  `重点航标` int(11) NULL DEFAULT NULL,
  `最后定级` int(11) NULL DEFAULT NULL,
  `报警时长` float NULL DEFAULT NULL,
  `重要程度` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `总时限` int(11) NULL DEFAULT NULL,
  `时限修正` int(11) NULL DEFAULT NULL,
  `重要程度排序` int(11) NULL DEFAULT NULL,
  `真失常时间` datetime NULL DEFAULT NULL,
  `真恢复时间` datetime NULL DEFAULT NULL,
  `失常登记准确性` int(11) NULL DEFAULT NULL,
  `失常恢复及时性` int(11) NULL DEFAULT NULL,
  `通告编号` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `维护船舶` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `到达现场时间` datetime NULL DEFAULT NULL,
  `现场距离` float NULL DEFAULT NULL,
  `基点经度` float NULL DEFAULT NULL,
  `基点纬度` float NULL DEFAULT NULL,
  `航道里程` float NULL DEFAULT NULL,
  PRIMARY KEY (`失常ID`) USING BTREE,
  UNIQUE INDEX `失常ID`(`失常ID`) USING BTREE,
  INDEX `ix_失常综合分析_hb_id`(`hb_id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for 水位完整率
-- ----------------------------
DROP TABLE IF EXISTS `水位完整率`;
CREATE TABLE `水位完整率`  (
  `ID` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `检查日期` date NULL DEFAULT NULL,
  `水位站` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `序号` int(11) NULL DEFAULT NULL,
  `总数` int(11) NULL DEFAULT NULL,
  `有数据数` int(11) NULL DEFAULT NULL,
  `完整率` float NULL DEFAULT NULL,
  PRIMARY KEY (`ID`) USING BTREE,
  UNIQUE INDEX `ID`(`ID`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for 水位数据异常
-- ----------------------------
DROP TABLE IF EXISTS `水位数据异常`;
CREATE TABLE `水位数据异常`  (
  `ID` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `水位站` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `测量时间` datetime NULL DEFAULT NULL,
  `水位` float NULL DEFAULT NULL,
  `差值` float NULL DEFAULT NULL,
  PRIMARY KEY (`ID`) USING BTREE,
  UNIQUE INDEX `ID`(`ID`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for 水位数据整点缺失
-- ----------------------------
DROP TABLE IF EXISTS `水位数据整点缺失`;
CREATE TABLE `水位数据整点缺失`  (
  `ID` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `水位站` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `缺失时间` datetime NULL DEFAULT NULL,
  PRIMARY KEY (`ID`) USING BTREE,
  UNIQUE INDEX `ID`(`ID`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for 水位正常率
-- ----------------------------
DROP TABLE IF EXISTS `水位正常率`;
CREATE TABLE `水位正常率`  (
  `ID` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `检查日期` date NULL DEFAULT NULL,
  `水位站` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `序号` int(11) NULL DEFAULT NULL,
  `总数` int(11) NULL DEFAULT NULL,
  `正常数` int(11) NULL DEFAULT NULL,
  `正常率` float NULL DEFAULT NULL,
  PRIMARY KEY (`ID`) USING BTREE,
  UNIQUE INDEX `ID`(`ID`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for 航标基础信息准确率
-- ----------------------------
DROP TABLE IF EXISTS `航标基础信息准确率`;
CREATE TABLE `航标基础信息准确率`  (
  `ID` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `检查日期` date NULL DEFAULT NULL,
  `单位` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `序号` int(11) NULL DEFAULT NULL,
  `公用航标数` int(11) NULL DEFAULT NULL,
  `航标基础数据设置错误数` int(11) NULL DEFAULT NULL,
  `准确率` float NULL DEFAULT NULL,
  PRIMARY KEY (`ID`) USING BTREE,
  UNIQUE INDEX `ID`(`ID`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for 航标基础信息错误明细
-- ----------------------------
DROP TABLE IF EXISTS `航标基础信息错误明细`;
CREATE TABLE `航标基础信息错误明细`  (
  `ID` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `检查日期` date NULL DEFAULT NULL,
  `单位` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `航标` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `标签` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `航标灯类型` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `厂家` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `位移阈值` float NULL DEFAULT NULL,
  `漂移阈值` float NULL DEFAULT NULL,
  `终端高电压阈值` float NULL DEFAULT NULL,
  `终端低电压阈值` float NULL DEFAULT NULL,
  `航标灯高电压阈值` float NULL DEFAULT NULL,
  `航标灯低电压阈值` float NULL DEFAULT NULL,
  `日光阈值` float NULL DEFAULT NULL,
  `轮询周期` float NULL DEFAULT NULL,
  `报警周期` float NULL DEFAULT NULL,
  `问题` text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL,
  PRIMARY KEY (`ID`) USING BTREE,
  UNIQUE INDEX `ID`(`ID`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for 航标监测未覆盖明细
-- ----------------------------
DROP TABLE IF EXISTS `航标监测未覆盖明细`;
CREATE TABLE `航标监测未覆盖明细`  (
  `ID` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `检查日期` date NULL DEFAULT NULL,
  `单位` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `航标` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `标签` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`ID`) USING BTREE,
  UNIQUE INDEX `ID`(`ID`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for 航标监测覆盖率
-- ----------------------------
DROP TABLE IF EXISTS `航标监测覆盖率`;
CREATE TABLE `航标监测覆盖率`  (
  `ID` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `检查日期` date NULL DEFAULT NULL,
  `单位` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `序号` int(11) NULL DEFAULT NULL,
  `应装` int(11) NULL DEFAULT NULL,
  `实装` int(11) NULL DEFAULT NULL,
  `覆盖率` float NULL DEFAULT NULL,
  PRIMARY KEY (`ID`) USING BTREE,
  UNIQUE INDEX `ID`(`ID`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for 调度不合格明细
-- ----------------------------
DROP TABLE IF EXISTS `调度不合格明细`;
CREATE TABLE `调度不合格明细`  (
  `ID` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `检查日期` date NULL DEFAULT NULL,
  `单位` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `航标` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `是否为重点航标` int(11) NULL DEFAULT NULL,
  `sim卡号` bigint(20) NULL DEFAULT NULL,
  `报警类型` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `报警时间` datetime NULL DEFAULT NULL,
  `报警消除时间` datetime NULL DEFAULT NULL,
  `报警时长` float NULL DEFAULT NULL,
  `调度阶段` int(11) NULL DEFAULT NULL,
  `定级建议` int(11) NULL DEFAULT NULL,
  `分类建议` int(11) NULL DEFAULT NULL,
  `调度时间` datetime NULL DEFAULT NULL,
  `调度详情` text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL,
  `实际定级` int(11) NULL DEFAULT NULL,
  `实际分类` int(11) NULL DEFAULT NULL,
  `调度类型` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `是否参照其他报警调度` int(11) NULL DEFAULT NULL,
  `首次参照时间` datetime NULL DEFAULT NULL,
  `最后调度时间` datetime NULL DEFAULT NULL,
  `最后调度详情` text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL,
  `最后定级` int(11) NULL DEFAULT NULL,
  `最后分类` int(11) NULL DEFAULT NULL,
  `最后调度类型` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `调度是否合格` int(11) NULL DEFAULT NULL,
  `报警ID` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `任务ID` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`ID`) USING BTREE,
  UNIQUE INDEX `ID`(`ID`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for 调度合格率
-- ----------------------------
DROP TABLE IF EXISTS `调度合格率`;
CREATE TABLE `调度合格率`  (
  `ID` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `检查日期` date NULL DEFAULT NULL,
  `调度合格数` int(11) NULL DEFAULT NULL,
  `调度总数` int(11) NULL DEFAULT NULL,
  `调度合格率` float NULL DEFAULT NULL,
  PRIMARY KEY (`ID`) USING BTREE,
  UNIQUE INDEX `ID`(`ID`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

SET FOREIGN_KEY_CHECKS = 1;
