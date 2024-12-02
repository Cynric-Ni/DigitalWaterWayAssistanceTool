/*
 Navicat Premium Data Transfer

 Source Server         : nas_sql
 Source Server Type    : MySQL
 Source Server Version : 50743
 Source Host           : 10.10.10.4:3306
 Source Schema         : 基础数据

 Target Server Type    : MySQL
 Target Server Version : 50743
 File Encoding         : 65001

 Date: 06/05/2024 08:39:40
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for 基层处
-- ----------------------------
DROP TABLE IF EXISTS `基层处`;
CREATE TABLE `基层处`  (
  `序号` int(11) NOT NULL,
  `单位` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`序号`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of 基层处
-- ----------------------------
INSERT INTO `基层处` VALUES (1, '大沙处');
INSERT INTO `基层处` VALUES (2, '簰洲处');
INSERT INTO `基层处` VALUES (3, '金口处');
INSERT INTO `基层处` VALUES (4, '武汉处');
INSERT INTO `基层处` VALUES (5, '阳逻处');
INSERT INTO `基层处` VALUES (6, '黄冈处');
INSERT INTO `基层处` VALUES (7, '黄石处');
INSERT INTO `基层处` VALUES (8, '蕲州处');
INSERT INTO `基层处` VALUES (9, '总计');

-- ----------------------------
-- Table structure for 失常类型
-- ----------------------------
DROP TABLE IF EXISTS `失常类型`;
CREATE TABLE `失常类型`  (
  `id` varchar(50) CHARACTER SET gbk COLLATE gbk_chinese_ci NULL DEFAULT NULL,
  `类型` varchar(255) CHARACTER SET gbk COLLATE gbk_chinese_ci NULL DEFAULT NULL
) ENGINE = InnoDB CHARACTER SET = gbk COLLATE = gbk_chinese_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of 失常类型
-- ----------------------------
INSERT INTO `失常类型` VALUES ('1', '标位失常');
INSERT INTO `失常类型` VALUES ('2', '标体失常');
INSERT INTO `失常类型` VALUES ('3', '灯器失常');

-- ----------------------------
-- Table structure for 报警类型
-- ----------------------------
DROP TABLE IF EXISTS `报警类型`;
CREATE TABLE `报警类型`  (
  `id` int(11) NOT NULL,
  `类型` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of 报警类型
-- ----------------------------
INSERT INTO `报警类型` VALUES (1, '终端故障');
INSERT INTO `报警类型` VALUES (2, '参数未同步');
INSERT INTO `报警类型` VALUES (3, '航标灯报警');
INSERT INTO `报警类型` VALUES (4, '灯通讯报警');
INSERT INTO `报警类型` VALUES (5, '电压报警');
INSERT INTO `报警类型` VALUES (6, '定位无效');
INSERT INTO `报警类型` VALUES (7, '位移报警');
INSERT INTO `报警类型` VALUES (8, '漂移报警');
INSERT INTO `报警类型` VALUES (9, '超时报警');
INSERT INTO `报警类型` VALUES (10, '终端电压报警');

-- ----------------------------
-- Table structure for 水位站
-- ----------------------------
DROP TABLE IF EXISTS `水位站`;
CREATE TABLE `水位站`  (
  `序号` int(11) NOT NULL,
  `站点名称` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`序号`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of 水位站
-- ----------------------------
INSERT INTO `水位站` VALUES (1, '莫家河（嘉鱼大桥）');
INSERT INTO `水位站` VALUES (2, '簰洲');
INSERT INTO `水位站` VALUES (3, '军山');
INSERT INTO `水位站` VALUES (4, '汉口（武汉关）');
INSERT INTO `水位站` VALUES (5, '阳逻');
INSERT INTO `水位站` VALUES (6, '鄂州');
INSERT INTO `水位站` VALUES (7, '黄石（黄石大桥）');
INSERT INTO `水位站` VALUES (8, '蕲春');

-- ----------------------------
-- Table structure for 水位站阈值
-- ----------------------------
DROP TABLE IF EXISTS `水位站阈值`;
CREATE TABLE `水位站阈值`  (
  `水位站ID` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `水位站` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `阈值` float NULL DEFAULT NULL,
  PRIMARY KEY (`水位站ID`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of 水位站阈值
-- ----------------------------
INSERT INTO `水位站阈值` VALUES ('1c713fb0747541a6b62b97a48bde32c5', '黄石（黄石大桥）', 0.8);
INSERT INTO `水位站阈值` VALUES ('4701d385bf6140ca96e5f72423797fbf', '军山', 0.8);
INSERT INTO `水位站阈值` VALUES ('55ead3582d34421a9a9f87594a7ab21b', '莫家河（嘉鱼大桥）', 0.8);
INSERT INTO `水位站阈值` VALUES ('6c31430921d8412f8f4516cecc2daa61', '阳逻', 0.8);
INSERT INTO `水位站阈值` VALUES ('a3ff4a3aa20c4f4ba10c8eddd5f0123e', '蕲春', 0.8);
INSERT INTO `水位站阈值` VALUES ('b8a7e37f0781445ab204a47ed8bf1f40', '汉口（武汉关）', 0.8);
INSERT INTO `水位站阈值` VALUES ('d8bdbd5ec26745558a77d2f744473536', '簰洲', 0.8);
INSERT INTO `水位站阈值` VALUES ('dc0aeb4035ab41fb861703ad4b950d4e', '鄂州', 0.8);

-- ----------------------------
-- Table structure for 电压阈值规定
-- ----------------------------
DROP TABLE IF EXISTS `电压阈值规定`;
CREATE TABLE `电压阈值规定`  (
  `理论终端低电压阈值` float NULL DEFAULT NULL,
  `理论终端高电压阈值` float NULL DEFAULT NULL,
  `理论航标灯低电压阈值` float NULL DEFAULT NULL,
  `理论航标灯高电压阈值` float NULL DEFAULT NULL,
  `航标灯类型` varchar(10) CHARACTER SET gbk COLLATE gbk_chinese_ci NULL DEFAULT NULL,
  `厂家` varchar(10) CHARACTER SET gbk COLLATE gbk_chinese_ci NULL DEFAULT NULL
) ENGINE = InnoDB CHARACTER SET = gbk COLLATE = gbk_chinese_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of 电压阈值规定
-- ----------------------------
INSERT INTO `电压阈值规定` VALUES (5.6, 12, 5.6, 12, '分体式', '吉星智能');
INSERT INTO `电压阈值规定` VALUES (12.5, 25, 12.5, 25, '一体化RTU', '吉星智能');
INSERT INTO `电压阈值规定` VALUES (6, 12, 6, 12, '分体式', '湖北蓝宇');
INSERT INTO `电压阈值规定` VALUES (12.5, 25, 12.5, 25, '一体化RTU', '湖北蓝宇');

-- ----------------------------
-- Table structure for 组织机构
-- ----------------------------
DROP TABLE IF EXISTS `组织机构`;
CREATE TABLE `组织机构`  (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `单位名称` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `单位` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `全路径` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `parent_id` int(11) NULL DEFAULT NULL,
  `所属单位` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`ID`) USING BTREE,
  UNIQUE INDEX `ix_组织机构_ID`(`ID`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1058803 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of 组织机构
-- ----------------------------
INSERT INTO `组织机构` VALUES (100, '长江航道局', '长江航道局', '长江航道局', NULL, '长江航道局');
INSERT INTO `组织机构` VALUES (105, '长江武汉航道局', '武汉局', '长江航道局/长江武汉航道局', 100, '长江武汉航道局');
INSERT INTO `组织机构` VALUES (112, '新OA测试部', '新OA测试部', '长江航道局/新OA测试部', 100, '新OA测试部');
INSERT INTO `组织机构` VALUES (10001, '局领导', '局领导', '长江航道局/局领导', 100, '长江航道局');
INSERT INTO `组织机构` VALUES (10002, '办公室', '办公室', '长江航道局/办公室', 100, '长江航道局');
INSERT INTO `组织机构` VALUES (10003, '政策法规处', '政策法规处', '长江航道局/政策法规处', 100, '长江航道局');
INSERT INTO `组织机构` VALUES (10004, '财务审计处', '财务审计处', '长江航道局/财务审计处', 100, '长江航道局');
INSERT INTO `组织机构` VALUES (10005, '人事教育处', '人事教育处', '长江航道局/人事教育处', 100, '长江航道局');
INSERT INTO `组织机构` VALUES (10006, '航道运行处(总值班室)', '航道运行处(总值班室)', '长江航道局/航道运行处(总值班室)', 100, '长江航道局');
INSERT INTO `组织机构` VALUES (10007, '航标处', '航标处', '长江航道局/航标处', 100, '长江航道局');
INSERT INTO `组织机构` VALUES (10008, '疏浚养护处', '疏浚养护处', '长江航道局/疏浚养护处', 100, '长江航道局');
INSERT INTO `组织机构` VALUES (10009, '测绘信息处', '测绘信息处', '长江航道局/测绘信息处', 100, '长江航道局');
INSERT INTO `组织机构` VALUES (10010, '技术服务处', '技术服务处', '长江航道局/技术服务处', 100, '长江航道局');
INSERT INTO `组织机构` VALUES (10011, '规划基建装备处', '规划基建装备处', '长江航道局/规划基建装备处', 100, '长江航道局');
INSERT INTO `组织机构` VALUES (10012, '安全与环境保护处', '安全与环境保护处', '长江航道局/安全与环境保护处', 100, '长江航道局');
INSERT INTO `组织机构` VALUES (10013, '党群办公室', '党群办公室', '长江航道局/党群办公室', 100, '长江航道局');
INSERT INTO `组织机构` VALUES (10014, '纪检监察处', '纪检监察处', '长江航道局/纪检监察处', 100, '长江航道局');
INSERT INTO `组织机构` VALUES (10501, '局机关', '武汉局', '长江航道局/长江武汉航道局/局机关', 105, '长江武汉航道局');
INSERT INTO `组织机构` VALUES (10502, '长江荆州航道处', '荆州处', '长江航道局/长江荆州航道处', 105, '长江荆州航道处');
INSERT INTO `组织机构` VALUES (10503, '长江公安航道处', '公安处', '长江航道局/长江荆州航道处/长江公安航道处', 105, '长江荆州航道处');
INSERT INTO `组织机构` VALUES (10504, '长江江陵航道处', '江陵处', '长江航道局/长江荆州航道处/长江江陵航道处', 105, '长江荆州航道处');
INSERT INTO `组织机构` VALUES (10505, '长江石首航道处', '石首处', '长江航道局/长江荆州航道处/长江石首航道处', 105, '长江荆州航道处');
INSERT INTO `组织机构` VALUES (10506, '长江调关航道处', '调关处', '长江航道局/长江荆州航道处/长江调关航道处', 10502, '长江荆州航道处');
INSERT INTO `组织机构` VALUES (10507, '长江岳阳航道处', '岳阳处', '长江航道局/长江岳阳航道处', 105, '长江岳阳航道处');
INSERT INTO `组织机构` VALUES (10508, '长江监利航道处', '监利处', '长江航道局/长江岳阳航道处/长江监利航道处', 105, '长江岳阳航道处');
INSERT INTO `组织机构` VALUES (10509, '长江铁铺航道处', '铁铺处', '长江航道局/长江岳阳航道处/长江铁铺航道处', 105, '长江岳阳航道处');
INSERT INTO `组织机构` VALUES (10510, '长江洪湖航道处', '洪湖处', '长江航道局/长江岳阳航道处/长江洪湖航道处', 105, '长江岳阳航道处');
INSERT INTO `组织机构` VALUES (10511, '长江武汉航道处', '武汉处', '长江航道局/长江武汉航道局/长江武汉航道处', 105, '长江武汉航道局');
INSERT INTO `组织机构` VALUES (10512, '长江大沙航道处', '大沙处', '长江航道局/长江武汉航道局/长江大沙航道处', 105, '长江武汉航道局');
INSERT INTO `组织机构` VALUES (10513, '长江簰洲航道处', '簰洲处', '长江航道局/长江武汉航道局/长江簰洲航道处', 105, '长江武汉航道局');
INSERT INTO `组织机构` VALUES (10514, '长江金口航道处', '金口处', '长江航道局/长江武汉航道局/长江金口航道处', 105, '长江武汉航道局');
INSERT INTO `组织机构` VALUES (10515, '长江阳逻航道处', '阳逻处', '长江航道局/长江武汉航道局/长江阳逻航道处', 105, '长江武汉航道局');
INSERT INTO `组织机构` VALUES (10516, '长江黄石航道处', '黄石处', '长江航道局/长江武汉航道局/长江黄石航道处', 105, '长江武汉航道局');
INSERT INTO `组织机构` VALUES (10517, '长江黄冈航道处', '黄冈处', '长江航道局/长江武汉航道局/长江黄冈航道处', 105, '长江武汉航道局');
INSERT INTO `组织机构` VALUES (10518, '长江蕲州航道处', '蕲州处', '长江航道局/长江武汉航道局/长江蕲州航道处', 105, '长江武汉航道局');
INSERT INTO `组织机构` VALUES (10519, '长江武汉航道局档案中心', '武汉局', '长江航道局/长江武汉航道局/长江武汉航道局档案中心', 105, '长江武汉航道局');
INSERT INTO `组织机构` VALUES (10520, '长江武汉航道局离退休\n职工服务中心', '武汉局', '长江航道局/长江武汉航道局/长江武汉航道局离退休\n职工服务中心', 105, '长江武汉航道局');
INSERT INTO `组织机构` VALUES (10521, '长江武汉航道局机关事务\n服务中心', '武汉局', '长江航道局/长江武汉航道局/长江武汉航道局机关事务\n服务中心', 105, '长江武汉航道局');
INSERT INTO `组织机构` VALUES (10522, '长江水工类工程公司筹备组', '长江水工类工程公司筹备组', '长江航道局/长江武汉航道局/长江水工类工程公司筹备组', 105, '长江武汉航道局');
INSERT INTO `组织机构` VALUES (10523, '荆州基地工作组', '荆州基地工作组', '长江航道局/长江荆州航道处/荆州基地工作组', 10502, '长江荆州航道处');
INSERT INTO `组织机构` VALUES (10524, '岳阳基地工作组', '岳阳基地工作组', '长江航道局/长江岳阳航道处/岳阳基地工作组', 10507, '长江岳阳航道处');
INSERT INTO `组织机构` VALUES (10588, '测试全能处', '武汉局', '长江航道局/长江武汉航道局/测试全能处', 105, '长江武汉航道局');
INSERT INTO `组织机构` VALUES (1050101, '局领导', '武汉局', '长江航道局/长江武汉航道局/局机关/局领导', 10501, '长江武汉航道局');
INSERT INTO `组织机构` VALUES (1050102, '办公室', '武汉局', '长江航道局/长江武汉航道局/局机关/办公室', 10501, '长江武汉航道局');
INSERT INTO `组织机构` VALUES (1050103, '财务审计处', '武汉局', '长江航道局/长江武汉航道局/局机关/财务审计处', 10501, '长江武汉航道局');
INSERT INTO `组织机构` VALUES (1050104, '人事教育处', '武汉局', '长江航道局/长江武汉航道局/局机关/人事教育处', 10501, '长江武汉航道局');
INSERT INTO `组织机构` VALUES (1050105, '航标处', '武汉局', '长江航道局/长江武汉航道局/局机关/航标处', 10501, '长江武汉航道局');
INSERT INTO `组织机构` VALUES (1050106, '测绘处', '武汉局', '长江航道局/长江武汉航道局/局机关/测绘处', 10501, '长江武汉航道局');
INSERT INTO `组织机构` VALUES (1050107, '航道运行处', '武汉局', '长江航道局/长江武汉航道局/局机关/航道运行处', 10501, '长江武汉航道局');
INSERT INTO `组织机构` VALUES (1050108, '规划基建处', '武汉局', '长江航道局/长江武汉航道局/局机关/规划基建处', 10501, '长江武汉航道局');
INSERT INTO `组织机构` VALUES (1050109, '资产装备处(安全处)', '武汉局', '长江航道局/长江武汉航道局/局机关/资产装备处(安全处)', 10501, '长江武汉航道局');
INSERT INTO `组织机构` VALUES (1050110, '党群办公室', '武汉局', '长江航道局/长江武汉航道局/局机关/党群办公室', 10501, '长江武汉航道局');
INSERT INTO `组织机构` VALUES (1050111, '纪检监察处', '武汉局', '长江航道局/长江武汉航道局/局机关/纪检监察处', 10501, '长江武汉航道局');
INSERT INTO `组织机构` VALUES (1050201, '荆州处领导', '荆州处', '长江航道局/长江荆州航道处/荆州处领导', 10502, '长江荆州航道处');
INSERT INTO `组织机构` VALUES (1050202, '荆州综合办公室', '荆州处', '长江航道局/长江荆州航道处/荆州综合办公室', 10502, '长江荆州航道处');
INSERT INTO `组织机构` VALUES (1050203, '荆州人事科', '荆州处', '长江航道局/长江荆州航道处/荆州人事科', 10502, '长江荆州航道处');
INSERT INTO `组织机构` VALUES (1050204, '荆州财务科', '荆州处', '长江航道局/长江荆州航道处/荆州财务科', 10502, '长江荆州航道处');
INSERT INTO `组织机构` VALUES (1050205, '荆州航道科', '荆州处', '长江航道局/长江荆州航道处/荆州航道科', 10502, '长江荆州航道处');
INSERT INTO `组织机构` VALUES (1050206, '荆州安全设备科', '荆州处', '长江航道局/长江荆州航道处/荆州安全设备科', 10502, '长江荆州航道处');
INSERT INTO `组织机构` VALUES (1050207, '荆州航道测绘中心', '荆州处', '长江航道局/长江荆州航道处/荆州航道测绘中心', 10502, '长江荆州航道处');
INSERT INTO `组织机构` VALUES (1050208, '荆州综合服务中心', '荆州处', '长江航道局/长江荆州航道处/荆州综合服务中心', 10502, '长江荆州航道处');
INSERT INTO `组织机构` VALUES (1050209, '荆桥维护基地', '荆桥基地', '长江航道局/长江荆州航道处/荆州基地工作组/荆桥维护基地', 10523, '长江荆州航道处');
INSERT INTO `组织机构` VALUES (1050210, '涴市维护基地', '涴市基地', '长江航道局/长江荆州航道处/荆州基地工作组/涴市维护基地', 10523, '长江荆州航道处');
INSERT INTO `组织机构` VALUES (1050301, '公安处领导', '公安处', '长江航道局/长江荆州航道处/长江公安航道处/公安处领导', 10503, '长江荆州航道处');
INSERT INTO `组织机构` VALUES (1050302, '公安综合办公室', '公安处', '长江航道局/长江荆州航道处/长江公安航道处/公安综合办公室', 10503, '长江荆州航道处');
INSERT INTO `组织机构` VALUES (1050303, '公安航道科', '公安处', '长江航道局/长江荆州航道处/长江公安航道处/公安航道科', 10503, '长江荆州航道处');
INSERT INTO `组织机构` VALUES (1050304, '公安航道运行监控中心（值班室）', '公安处', '长江航道局/长江荆州航道处/长江公安航道处/公安航道运行监控中心（值班室）', 10503, '长江荆州航道处');
INSERT INTO `组织机构` VALUES (1050305, '公安班组', '公安处', '长江航道局/长江荆州航道处/长江公安航道处/公安班组', 10503, '长江荆州航道处');
INSERT INTO `组织机构` VALUES (1050401, '江陵处领导', '江陵处', '长江航道局/长江荆州航道处/长江江陵航道处/江陵处领导', 10504, '长江荆州航道处');
INSERT INTO `组织机构` VALUES (1050402, '江陵综合办公室', '江陵处', '长江航道局/长江荆州航道处/长江江陵航道处/江陵综合办公室', 10504, '长江荆州航道处');
INSERT INTO `组织机构` VALUES (1050403, '江陵航道科', '江陵处', '长江航道局/长江荆州航道处/长江江陵航道处/江陵航道科', 10504, '长江荆州航道处');
INSERT INTO `组织机构` VALUES (1050404, '江陵航道运行监控中心（值班室）', '江陵处', '长江航道局/长江荆州航道处/长江江陵航道处/江陵航道运行监控中心（值班室）', 10504, '长江荆州航道处');
INSERT INTO `组织机构` VALUES (1050405, '江陵班组', '江陵处', '长江航道局/长江荆州航道处/长江江陵航道处/江陵班组', 10504, '长江荆州航道处');
INSERT INTO `组织机构` VALUES (1050501, '石首处领导', '石首处', '长江航道局/长江荆州航道处/长江石首航道处/石首处领导', 10505, '长江荆州航道处');
INSERT INTO `组织机构` VALUES (1050502, '石首综合办公室', '石首处', '长江航道局/长江荆州航道处/长江石首航道处/石首综合办公室', 10505, '长江荆州航道处');
INSERT INTO `组织机构` VALUES (1050503, '石首航道科', '石首处', '长江航道局/长江荆州航道处/长江石首航道处/石首航道科', 10505, '长江荆州航道处');
INSERT INTO `组织机构` VALUES (1050504, '石首航道运行监控中心（值班室）', '石首处', '长江航道局/长江荆州航道处/长江石首航道处/石首航道运行监控中心（值班室）', 10505, '长江荆州航道处');
INSERT INTO `组织机构` VALUES (1050505, '石首班组', '石首处', '长江航道局/长江荆州航道处/长江石首航道处/石首班组', 10505, '长江荆州航道处');
INSERT INTO `组织机构` VALUES (1050601, '调关处领导', '调关处', '长江航道局/长江荆州航道处/长江调关航道处/调关处领导', 10506, '长江荆州航道处');
INSERT INTO `组织机构` VALUES (1050602, '调关综合办公室', '调关处', '长江航道局/长江荆州航道处/长江调关航道处/调关综合办公室', 10506, '长江荆州航道处');
INSERT INTO `组织机构` VALUES (1050603, '调关航道科', '调关处', '长江航道局/长江荆州航道处/长江调关航道处/调关航道科', 10506, '长江荆州航道处');
INSERT INTO `组织机构` VALUES (1050604, '调关航道运行监控中心（值班室）', '调关处', '长江航道局/长江荆州航道处/长江调关航道处/调关航道运行监控中心（值班室）', 10506, '长江荆州航道处');
INSERT INTO `组织机构` VALUES (1050605, '调关班组', '调关处', '长江航道局/长江荆州航道处/长江调关航道处/调关班组', 10506, '长江荆州航道处');
INSERT INTO `组织机构` VALUES (1050701, '岳阳处领导', '岳阳处', '长江航道局/长江岳阳航道处/岳阳处领导', 10507, '长江岳阳航道处');
INSERT INTO `组织机构` VALUES (1050702, '岳阳综合办公室', '岳阳处', '长江航道局/长江岳阳航道处/岳阳综合办公室', 10507, '长江岳阳航道处');
INSERT INTO `组织机构` VALUES (1050703, '岳阳人事科', '岳阳处', '长江航道局/长江岳阳航道处/岳阳人事科', 10507, '长江岳阳航道处');
INSERT INTO `组织机构` VALUES (1050704, '岳阳财务科', '岳阳处', '长江航道局/长江岳阳航道处/岳阳财务科', 10507, '长江岳阳航道处');
INSERT INTO `组织机构` VALUES (1050705, '岳阳航道科', '岳阳处', '长江航道局/长江岳阳航道处/岳阳航道科', 10507, '长江岳阳航道处');
INSERT INTO `组织机构` VALUES (1050706, '岳阳安全设备科', '岳阳处', '长江航道局/长江岳阳航道处/岳阳安全设备科', 10507, '长江岳阳航道处');
INSERT INTO `组织机构` VALUES (1050707, '岳阳航道测绘中心', '岳阳处', '长江航道局/长江岳阳航道处/岳阳航道测绘中心', 10507, '长江岳阳航道处');
INSERT INTO `组织机构` VALUES (1050708, '岳阳综合服务中心（航标器材维修中心）', '岳阳处', '长江航道局/长江岳阳航道处/岳阳综合服务中心（航标器材维修中心）', 10507, '长江岳阳航道处');
INSERT INTO `组织机构` VALUES (1050709, '城陵矶航道维护基地', '城陵矶基地', '长江航道局/长江岳阳航道处/岳阳基地工作组/城陵矶航道维护基地', 10524, '长江岳阳航道处');
INSERT INTO `组织机构` VALUES (1050710, '道仁矶航道维护基地', '道仁矶基地', '长江航道局/长江岳阳航道处/岳阳基地工作组/道仁矶航道维护基地', 10524, '长江岳阳航道处');
INSERT INTO `组织机构` VALUES (1050801, '监利处领导', '监利处', '长江航道局/长江岳阳航道处/长江监利航道处/监利处领导', 10508, '长江岳阳航道处');
INSERT INTO `组织机构` VALUES (1050802, '监利处综合办公室', '监利处', '长江航道局/长江岳阳航道处/长江监利航道处/监利处综合办公室', 10508, '长江岳阳航道处');
INSERT INTO `组织机构` VALUES (1050803, '监利处航道科', '监利处', '长江航道局/长江岳阳航道处/长江监利航道处/监利处航道科', 10508, '长江岳阳航道处');
INSERT INTO `组织机构` VALUES (1050804, '监利航标器材维修中心', '监利处', '长江航道局/长江岳阳航道处/长江监利航道处/监利航标器材维修中心', 10508, '长江岳阳航道处');
INSERT INTO `组织机构` VALUES (1050805, '监利班组', '监利处', '长江航道局/长江岳阳航道处/长江监利航道处/监利班组', 10508, '长江岳阳航道处');
INSERT INTO `组织机构` VALUES (1050806, '监利综合服务中心', '监利处', '长江航道局/长江岳阳航道处/长江监利航道处/监利综合服务中心', 10508, '长江岳阳航道处');
INSERT INTO `组织机构` VALUES (1050901, '铁铺处领导', '铁铺处', '长江航道局/长江岳阳航道处/长江铁铺航道处/铁铺处领导', 10509, '长江岳阳航道处');
INSERT INTO `组织机构` VALUES (1050902, '铁铺综合办公室', '铁铺处', '长江航道局/长江岳阳航道处/长江铁铺航道处/铁铺综合办公室', 10509, '长江岳阳航道处');
INSERT INTO `组织机构` VALUES (1050903, '铁铺航道科', '铁铺处', '长江航道局/长江岳阳航道处/长江铁铺航道处/铁铺航道科', 10509, '长江岳阳航道处');
INSERT INTO `组织机构` VALUES (1050904, '铁铺航道运行监控中心（值班室）', '铁铺处', '长江航道局/长江岳阳航道处/长江铁铺航道处/铁铺航道运行监控中心（值班室）', 10509, '长江岳阳航道处');
INSERT INTO `组织机构` VALUES (1050905, '铁铺班组', '铁铺处', '长江航道局/长江岳阳航道处/长江铁铺航道处/铁铺班组', 10509, '长江岳阳航道处');
INSERT INTO `组织机构` VALUES (1051001, '洪湖处领导', '洪湖处', '长江航道局/长江岳阳航道处/长江洪湖航道处/洪湖处领导', 10510, '长江岳阳航道处');
INSERT INTO `组织机构` VALUES (1051002, '洪湖综合办公室', '洪湖处', '长江航道局/长江岳阳航道处/长江洪湖航道处/洪湖综合办公室', 10510, '长江岳阳航道处');
INSERT INTO `组织机构` VALUES (1051003, '洪湖航道科', '洪湖处', '长江航道局/长江岳阳航道处/长江洪湖航道处/洪湖航道科', 10510, '长江岳阳航道处');
INSERT INTO `组织机构` VALUES (1051004, '洪湖综合服务中心', '洪湖处', '长江航道局/长江岳阳航道处/长江洪湖航道处/洪湖综合服务中心', 10510, '长江岳阳航道处');
INSERT INTO `组织机构` VALUES (1051005, '洪湖班组', '洪湖处', '长江航道局/长江岳阳航道处/长江洪湖航道处/洪湖班组', 10510, '长江岳阳航道处');
INSERT INTO `组织机构` VALUES (1051006, '洪湖航标器材维修中心', '洪湖处', '长江航道局/长江岳阳航道处/长江洪湖航道处/洪湖航标器材维修中心', 10510, '长江岳阳航道处');
INSERT INTO `组织机构` VALUES (1051101, '武汉处领导', '武汉处', '长江航道局/长江武汉航道局/长江武汉航道处/武汉处领导', 10511, '长江武汉航道局');
INSERT INTO `组织机构` VALUES (1051102, '武汉综合办公室', '武汉处', '长江航道局/长江武汉航道局/长江武汉航道处/武汉综合办公室', 10511, '长江武汉航道局');
INSERT INTO `组织机构` VALUES (1051103, '武汉人事科', '武汉处', '长江航道局/长江武汉航道局/长江武汉航道处/武汉人事科', 10511, '长江武汉航道局');
INSERT INTO `组织机构` VALUES (1051104, '武汉财务科', '武汉处', '长江航道局/长江武汉航道局/长江武汉航道处/武汉财务科', 10511, '长江武汉航道局');
INSERT INTO `组织机构` VALUES (1051105, '武汉航道科', '武汉处', '长江航道局/长江武汉航道局/长江武汉航道处/武汉航道科', 10511, '长江武汉航道局');
INSERT INTO `组织机构` VALUES (1051106, '武汉安全设备科', '武汉处', '长江航道局/长江武汉航道局/长江武汉航道处/武汉安全设备科', 10511, '长江武汉航道局');
INSERT INTO `组织机构` VALUES (1051107, '武汉航道测绘中心', '武汉局', '长江航道局/长江武汉航道局/武汉航道测绘中心', 105, '长江武汉航道局');
INSERT INTO `组织机构` VALUES (1051108, '武汉综合服务中心（航标器材维修中心）', '武汉处', '长江航道局/长江武汉航道局/长江武汉航道处/武汉综合服务中心（航标器材维修中心）', 10511, '长江武汉航道局');
INSERT INTO `组织机构` VALUES (1051109, '杨泗港基地', '武汉处', '长江航道局/长江武汉航道局/长江武汉航道处/杨泗港基地', 10511, '长江武汉航道局');
INSERT INTO `组织机构` VALUES (1051110, '天桥基地', '武汉处', '长江航道局/长江武汉航道局/长江武汉航道处/天桥基地', 10511, '长江武汉航道局');
INSERT INTO `组织机构` VALUES (1051111, '武汉班组', '武汉处', '长江航道局/长江武汉航道局/长江武汉航道处/武汉班组', 10511, '长江武汉航道局');
INSERT INTO `组织机构` VALUES (1051201, '大沙处领导', '大沙处', '长江航道局/长江武汉航道局/长江大沙航道处/大沙处领导', 10512, '长江武汉航道局');
INSERT INTO `组织机构` VALUES (1051202, '大沙综合办公室', '大沙处', '长江航道局/长江武汉航道局/长江大沙航道处/大沙综合办公室', 10512, '长江武汉航道局');
INSERT INTO `组织机构` VALUES (1051203, '大沙航道科', '大沙处', '长江航道局/长江武汉航道局/长江大沙航道处/大沙航道科', 10512, '长江武汉航道局');
INSERT INTO `组织机构` VALUES (1051204, '大沙航道运行监控中心（值班室）', '大沙处', '长江航道局/长江武汉航道局/长江大沙航道处/大沙航道运行监控中心（值班室）', 10512, '长江武汉航道局');
INSERT INTO `组织机构` VALUES (1051205, '大沙班组', '大沙处', '长江航道局/长江武汉航道局/长江大沙航道处/大沙班组', 10512, '长江武汉航道局');
INSERT INTO `组织机构` VALUES (1051301, '簰洲处领导', '簰洲处', '长江航道局/长江武汉航道局/长江簰洲航道处/簰洲处领导', 10513, '长江武汉航道局');
INSERT INTO `组织机构` VALUES (1051302, '簰洲综合办公室', '簰洲处', '长江航道局/长江武汉航道局/长江簰洲航道处/簰洲综合办公室', 10513, '长江武汉航道局');
INSERT INTO `组织机构` VALUES (1051303, '簰洲航道科', '簰洲处', '长江航道局/长江武汉航道局/长江簰洲航道处/簰洲航道科', 10513, '长江武汉航道局');
INSERT INTO `组织机构` VALUES (1051304, '簰洲航道运行监控中心（值班室）', '簰洲处', '长江航道局/长江武汉航道局/长江簰洲航道处/簰洲航道运行监控中心（值班室）', 10513, '长江武汉航道局');
INSERT INTO `组织机构` VALUES (1051305, '簰洲班组', '簰洲处', '长江航道局/长江武汉航道局/长江簰洲航道处/簰洲班组', 10513, '长江武汉航道局');
INSERT INTO `组织机构` VALUES (1051401, '金口处领导', '金口处', '长江航道局/长江武汉航道局/长江金口航道处/金口处领导', 10514, '长江武汉航道局');
INSERT INTO `组织机构` VALUES (1051402, '金口综合办公室', '金口处', '长江航道局/长江武汉航道局/长江金口航道处/金口综合办公室', 10514, '长江武汉航道局');
INSERT INTO `组织机构` VALUES (1051403, '金口航道科', '金口处', '长江航道局/长江武汉航道局/长江金口航道处/金口航道科', 10514, '长江武汉航道局');
INSERT INTO `组织机构` VALUES (1051404, '金口航道运行监控中心（值班室）', '金口处', '长江航道局/长江武汉航道局/长江金口航道处/金口航道运行监控中心（值班室）', 10514, '长江武汉航道局');
INSERT INTO `组织机构` VALUES (1051405, '金口班组', '金口处', '长江航道局/长江武汉航道局/长江金口航道处/金口班组', 10514, '长江武汉航道局');
INSERT INTO `组织机构` VALUES (1051501, '阳逻处领导', '阳逻处', '长江航道局/长江武汉航道局/长江阳逻航道处/阳逻处领导', 10515, '长江武汉航道局');
INSERT INTO `组织机构` VALUES (1051502, '阳逻综合办公室', '阳逻处', '长江航道局/长江武汉航道局/长江阳逻航道处/阳逻综合办公室', 10515, '长江武汉航道局');
INSERT INTO `组织机构` VALUES (1051503, '阳逻航道科', '阳逻处', '长江航道局/长江武汉航道局/长江阳逻航道处/阳逻航道科', 10515, '长江武汉航道局');
INSERT INTO `组织机构` VALUES (1051504, '阳逻航道运行监控中心（值班室）', '阳逻处', '长江航道局/长江武汉航道局/长江阳逻航道处/阳逻航道运行监控中心（值班室）', 10515, '长江武汉航道局');
INSERT INTO `组织机构` VALUES (1051505, '阳逻班组', '阳逻处', '长江航道局/长江武汉航道局/长江阳逻航道处/阳逻班组', 10515, '长江武汉航道局');
INSERT INTO `组织机构` VALUES (1051601, '黄石处领导', '黄石处', '长江航道局/长江武汉航道局/长江黄石航道处/黄石处领导', 10516, '长江武汉航道局');
INSERT INTO `组织机构` VALUES (1051602, '黄石综合办公室', '黄石处', '长江航道局/长江武汉航道局/长江黄石航道处/黄石综合办公室', 10516, '长江武汉航道局');
INSERT INTO `组织机构` VALUES (1051603, '黄石人事科', '黄石处', '长江航道局/长江武汉航道局/长江黄石航道处/黄石人事科', 10516, '长江武汉航道局');
INSERT INTO `组织机构` VALUES (1051604, '黄石财务科', '黄石处', '长江航道局/长江武汉航道局/长江黄石航道处/黄石财务科', 10516, '长江武汉航道局');
INSERT INTO `组织机构` VALUES (1051605, '黄石航道科', '黄石处', '长江航道局/长江武汉航道局/长江黄石航道处/黄石航道科', 10516, '长江武汉航道局');
INSERT INTO `组织机构` VALUES (1051606, '黄石安全设备科', '黄石处', '长江航道局/长江武汉航道局/长江黄石航道处/黄石安全设备科', 10516, '长江武汉航道局');
INSERT INTO `组织机构` VALUES (1051607, '黄石航道测绘中心', '黄石测绘中心', '长江航道局/长江武汉航道局/黄石航道测绘中心', 105, '长江武汉航道局');
INSERT INTO `组织机构` VALUES (1051608, '黄石综合服务中心(航标器材维修中心)', '黄石处', '长江航道局/长江武汉航道局/长江黄石航道处/黄石综合服务中心(航标器材维修中心)', 10516, '长江武汉航道局');
INSERT INTO `组织机构` VALUES (1051609, '黄石航道养护人员', '黄石处', '长江航道局/长江武汉航道局/长江黄石航道处/黄石航道养护人员', 10516, '长江武汉航道局');
INSERT INTO `组织机构` VALUES (1051610, '黄石班组', '黄石处', '长江航道局/长江武汉航道局/长江黄石航道处/黄石班组', 10516, '长江武汉航道局');
INSERT INTO `组织机构` VALUES (1051701, '黄冈处领导', '黄冈处', '长江航道局/长江武汉航道局/长江黄冈航道处/黄冈处领导', 10517, '长江武汉航道局');
INSERT INTO `组织机构` VALUES (1051702, '黄冈综合办公室', '黄冈处', '长江航道局/长江武汉航道局/长江黄冈航道处/黄冈综合办公室', 10517, '长江武汉航道局');
INSERT INTO `组织机构` VALUES (1051703, '黄冈航道科', '黄冈处', '长江航道局/长江武汉航道局/长江黄冈航道处/黄冈航道科', 10517, '长江武汉航道局');
INSERT INTO `组织机构` VALUES (1051704, '黄冈航道运行监控中心（值班室）', '黄冈处', '长江航道局/长江武汉航道局/长江黄冈航道处/黄冈航道运行监控中心（值班室）', 10517, '长江武汉航道局');
INSERT INTO `组织机构` VALUES (1051705, '黄冈班组', '黄冈处', '长江航道局/长江武汉航道局/长江黄冈航道处/黄冈班组', 10517, '长江武汉航道局');
INSERT INTO `组织机构` VALUES (1051801, '蕲州处领导', '蕲州处', '长江航道局/长江武汉航道局/长江蕲州航道处/蕲州处领导', 10518, '长江武汉航道局');
INSERT INTO `组织机构` VALUES (1051802, '蕲州综合办公室', '蕲州处', '长江航道局/长江武汉航道局/长江蕲州航道处/蕲州综合办公室', 10518, '长江武汉航道局');
INSERT INTO `组织机构` VALUES (1051803, '蕲州航道科', '蕲州处', '长江航道局/长江武汉航道局/长江蕲州航道处/蕲州航道科', 10518, '长江武汉航道局');
INSERT INTO `组织机构` VALUES (1051804, '蕲州航道运行监控中心（值班室）', '蕲州处', '长江航道局/长江武汉航道局/长江蕲州航道处/蕲州航道运行监控中心（值班室）', 10518, '长江武汉航道局');
INSERT INTO `组织机构` VALUES (1051805, '蕲州班组', '蕲州处', '长江航道局/长江武汉航道局/长江蕲州航道处/蕲州班组', 10518, '长江武汉航道局');
INSERT INTO `组织机构` VALUES (1052001, '离退中心领导', '武汉局', '长江航道局/长江武汉航道局/长江武汉航道局离退休\n职工服务中心/离退中心领导', 10520, '长江武汉航道局');
INSERT INTO `组织机构` VALUES (1052002, '离退中心办公室', '武汉局', '长江航道局/长江武汉航道局/长江武汉航道局离退休\n职工服务中心/离退中心办公室', 10520, '长江武汉航道局');
INSERT INTO `组织机构` VALUES (1052003, '离退中心财务科', '武汉局', '长江航道局/长江武汉航道局/长江武汉航道局离退休\n职工服务中心/离退中心财务科', 10520, '长江武汉航道局');
INSERT INTO `组织机构` VALUES (1052004, '离退休职工服务科', '武汉局', '长江航道局/长江武汉航道局/长江武汉航道局离退休\n职工服务中心/离退休职工服务科', 10520, '长江武汉航道局');
INSERT INTO `组织机构` VALUES (1052101, '机关事务服务中心领导', '武汉局', '长江航道局/长江武汉航道局/长江武汉航道局机关事务\n服务中心/机关事务服务中心领导', 10521, '长江武汉航道局');
INSERT INTO `组织机构` VALUES (1052102, '机关事务服务中心综合部', '武汉局', '长江航道局/长江武汉航道局/长江武汉航道局离退休\n职工服务中心/离退休职工服务科/机关事务服务中心综合部', 1052004, '长江武汉航道局');
INSERT INTO `组织机构` VALUES (1052103, '机关事务服务中心事务一部', '武汉局', '长江航道局/长江武汉航道局/长江武汉航道局机关事务\n服务中心/机关事务服务中心事务一部', 10521, '长江武汉航道局');
INSERT INTO `组织机构` VALUES (1052104, '机关事务服务中心事务二部', '武汉局', '长江航道局/长江武汉航道局/长江武汉航道局机关事务\n服务中心/机关事务服务中心事务二部', 10521, '长江武汉航道局');
INSERT INTO `组织机构` VALUES (1052105, '机关事务服务中心财务部', '武汉局', '长江航道局/长江武汉航道局/长江武汉航道局机关事务\n服务中心/机关事务服务中心财务部', 10521, '长江武汉航道局');
INSERT INTO `组织机构` VALUES (1052106, '机关事务服务中心物资部', '武汉局', '长江航道局/长江武汉航道局/长江武汉航道局机关事务\n服务中心/机关事务服务中心物资部', 10521, '长江武汉航道局');
INSERT INTO `组织机构` VALUES (1052107, '机关事务服务中心经营部', '武汉局', '长江航道局/长江武汉航道局/长江武汉航道局机关事务\n服务中心/机关事务服务中心经营部', 10521, '长江武汉航道局');
INSERT INTO `组织机构` VALUES (1052108, '机关事务服务中心小车班', '武汉局', '长江航道局/长江武汉航道局/长江武汉航道局机关事务\n服务中心/机关事务服务中心小车班', 10521, '长江武汉航道局');
INSERT INTO `组织机构` VALUES (1052109, '机关事务服务中心数字航道监控中心', '武汉局', '长江航道局/长江武汉航道局/长江武汉航道局机关事务\n服务中心/机关事务服务中心数字航道监控中心', 10521, '长江武汉航道局');
INSERT INTO `组织机构` VALUES (1052201, '公司筹备组领导', '长江水工类工程公司筹备组', '长江航道局/长江武汉航道局/长江水工类工程公司筹备组/公司筹备组领导', 10522, '长江武汉航道局');
INSERT INTO `组织机构` VALUES (1052202, '行政管理专项组', '长江水工类工程公司筹备组', '长江航道局/长江武汉航道局/长江水工类工程公司筹备组/行政管理专项组', 10522, '长江武汉航道局');
INSERT INTO `组织机构` VALUES (1052203, '党群工作专项组', '长江水工类工程公司筹备组', '长江航道局/长江武汉航道局/长江水工类工程公司筹备组/党群工作专项组', 10522, '长江武汉航道局');
INSERT INTO `组织机构` VALUES (1052204, '财务管理专项组', '长江水工类工程公司筹备组', '长江航道局/长江武汉航道局/长江水工类工程公司筹备组/财务管理专项组', 10522, '长江武汉航道局');
INSERT INTO `组织机构` VALUES (1052205, '人事管理专项组', '长江水工类工程公司筹备组', '长江航道局/长江武汉航道局/长江水工类工程公司筹备组/人事管理专项组', 10522, '长江武汉航道局');
INSERT INTO `组织机构` VALUES (1052206, '工程经营专项组', '长江水工类工程公司筹备组', '长江航道局/长江武汉航道局/长江水工类工程公司筹备组/工程经营专项组', 10522, '长江武汉航道局');
INSERT INTO `组织机构` VALUES (1052207, '安全设备专项组', '长江水工类工程公司筹备组', '长江航道局/长江武汉航道局/长江水工类工程公司筹备组/安全设备专项组', 10522, '长江武汉航道局');
INSERT INTO `组织机构` VALUES (1052208, '综合码头', '长江水工类工程公司筹备组', '长江航道局/长江武汉航道局/长江水工类工程公司筹备组/综合码头', 10522, '长江武汉航道局');
INSERT INTO `组织机构` VALUES (1052209, '经营管理部', '长江水工类工程公司筹备组', '长江航道局/长江武汉航道局/长江水工类工程公司筹备组/经营管理部', 10522, '长江武汉航道局');
INSERT INTO `组织机构` VALUES (1058801, '测试职能处', '武汉局', '长江航道局/长江武汉航道局/测试全能处/测试职能处', 10588, '长江武汉航道局');
INSERT INTO `组织机构` VALUES (1058802, '测试全能部门', '武汉局', '长江航道局/长江武汉航道局/测试全能处/测试全能部门', 10588, '长江武汉航道局');

-- ----------------------------
-- Table structure for 航标报警分析
-- ----------------------------
DROP TABLE IF EXISTS `航标报警分析`;
CREATE TABLE `航标报警分析`  (
  `序号` int(11) NULL DEFAULT NULL,
  `异常编号` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `异常种类` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `异常原因包括` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `异常原因排除` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `浮标` int(11) NULL DEFAULT NULL,
  `重点航标` int(11) NULL DEFAULT NULL,
  `夜间` int(11) NULL DEFAULT NULL,
  `异常时长下限` int(11) NULL DEFAULT NULL,
  `异常时长上限` int(11) NULL DEFAULT NULL,
  `降级处置类别` int(11) NULL DEFAULT NULL,
  `参考定级` int(11) NULL DEFAULT NULL,
  `参考分类` int(11) NULL DEFAULT NULL,
  `阶段截止时限` int(11) NULL DEFAULT NULL,
  `总时限` int(11) NULL DEFAULT NULL,
  `潮汐河段时限` int(11) NULL DEFAULT NULL,
  `时限修正` int(11) NULL DEFAULT NULL,
  `重要程度` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `对照编号` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `最早调度时限` int(11) NULL DEFAULT NULL,
  `最晚调度时限` int(11) NULL DEFAULT NULL
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of 航标报警分析
-- ----------------------------
INSERT INTO `航标报警分析` VALUES (1, 'A11', '8', NULL, NULL, 1, NULL, NULL, NULL, NULL, NULL, 1, 1, 210, 210, 330, NULL, 'A', NULL, 0, 30);
INSERT INTO `航标报警分析` VALUES (3, 'A12', '7', NULL, NULL, 1, 1, NULL, NULL, NULL, NULL, 1, 1, 210, 210, 330, NULL, 'A', NULL, 0, 30);
INSERT INTO `航标报警分析` VALUES (5, 'A13', '7', NULL, NULL, 1, 0, NULL, 150, NULL, NULL, 1, 1, 330, 330, NULL, NULL, 'A', NULL, 30, 180);
INSERT INTO `航标报警分析` VALUES (7, 'A21', '3', NULL, NULL, NULL, NULL, 1, 30, NULL, NULL, 1, 1, 210, 210, NULL, NULL, 'A', NULL, 30, 60);
INSERT INTO `航标报警分析` VALUES (9, 'A22', '4', NULL, NULL, NULL, NULL, NULL, 150, NULL, NULL, 1, 1, 330, 330, NULL, NULL, 'A', NULL, 30, 180);
INSERT INTO `航标报警分析` VALUES (11, 'A31', '9', NULL, NULL, NULL, NULL, NULL, 150, NULL, NULL, 1, 1, 330, 330, NULL, NULL, 'A', NULL, 30, 180);
INSERT INTO `航标报警分析` VALUES (13, 'A41', '6', NULL, NULL, 1, NULL, NULL, 150, NULL, NULL, 1, 1, 330, 330, NULL, NULL, 'A', NULL, 30, 180);
INSERT INTO `航标报警分析` VALUES (15, 'B11', '7', NULL, NULL, 1, 0, NULL, NULL, 150, NULL, 2, 2, 150, 330, NULL, NULL, 'B', NULL, NULL, NULL);
INSERT INTO `航标报警分析` VALUES (16, 'B21', '3', NULL, NULL, NULL, NULL, 0, 30, NULL, NULL, 2, 2, 330, 330, NULL, NULL, 'B', NULL, 30, 60);
INSERT INTO `航标报警分析` VALUES (18, 'B22', '4', NULL, NULL, NULL, NULL, NULL, 30, 150, NULL, 2, 2, 150, 330, NULL, NULL, 'B', NULL, NULL, NULL);
INSERT INTO `航标报警分析` VALUES (19, 'B23', '5', '检测航标灯工作低电压报警', NULL, NULL, NULL, NULL, NULL, NULL, NULL, 2, 3, 1440, 1440, NULL, NULL, 'B', NULL, 0, 30);
INSERT INTO `航标报警分析` VALUES (20, 'B23', '5', '请更换电池', NULL, NULL, NULL, NULL, NULL, NULL, NULL, 2, 3, 1440, 1440, NULL, NULL, 'B', NULL, 0, 30);
INSERT INTO `航标报警分析` VALUES (23, 'C25', '5', '检查充电控制器', NULL, NULL, NULL, NULL, NULL, NULL, NULL, 2, 3, 1440, 1440, NULL, NULL, 'B', NULL, NULL, NULL);
INSERT INTO `航标报警分析` VALUES (24, 'B42', '10', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 2, 3, 1440, 1440, NULL, NULL, 'B', NULL, NULL, NULL);
INSERT INTO `航标报警分析` VALUES (25, 'B31', '9', NULL, NULL, NULL, NULL, NULL, 30, 150, NULL, 2, 2, 150, 330, NULL, NULL, 'B', NULL, NULL, NULL);
INSERT INTO `航标报警分析` VALUES (26, 'B41', '6', NULL, NULL, 1, NULL, NULL, 30, 150, NULL, 2, 2, 150, 330, NULL, NULL, 'B', NULL, NULL, NULL);
INSERT INTO `航标报警分析` VALUES (27, 'B42', '5', '检测终端工作低电压报警', '检测航标灯工作低电压报警', NULL, NULL, NULL, NULL, NULL, NULL, 2, 3, 1440, 1440, NULL, NULL, 'B', NULL, 0, 30);
INSERT INTO `航标报警分析` VALUES (29, 'C11', '8', NULL, NULL, 2, NULL, NULL, NULL, NULL, NULL, 3, 3, 1440, 1440, NULL, NULL, 'C', NULL, 0, 30);
INSERT INTO `航标报警分析` VALUES (31, 'C11', '7', NULL, NULL, 2, NULL, NULL, NULL, NULL, NULL, 3, 3, 1440, 1440, NULL, NULL, 'C', NULL, 0, 30);
INSERT INTO `航标报警分析` VALUES (33, 'C12', '7', NULL, NULL, 1, 1, NULL, NULL, NULL, 2, 3, 4, 210, 210, NULL, NULL, 'A', NULL, NULL, NULL);
INSERT INTO `航标报警分析` VALUES (35, 'C13', '7', NULL, NULL, 1, 0, NULL, 150, NULL, 2, 3, 4, 330, 330, NULL, NULL, 'A', NULL, 150, 180);
INSERT INTO `航标报警分析` VALUES (37, 'C21', '3', NULL, NULL, NULL, NULL, 1, NULL, 30, NULL, 3, 4, 30, 210, NULL, NULL, 'C', NULL, NULL, NULL);
INSERT INTO `航标报警分析` VALUES (38, 'C22', '3', NULL, NULL, NULL, NULL, 0, NULL, 30, NULL, 3, 4, 30, 330, NULL, NULL, 'C', NULL, NULL, NULL);
INSERT INTO `航标报警分析` VALUES (39, 'C23', '4', NULL, NULL, NULL, NULL, NULL, NULL, 30, NULL, 3, 4, 30, 330, NULL, NULL, 'C', NULL, NULL, NULL);
INSERT INTO `航标报警分析` VALUES (40, 'C24', '4', NULL, NULL, NULL, NULL, NULL, 30, NULL, 1, 3, 3, 1400, 1440, NULL, 330, 'A', 'A22', NULL, NULL);
INSERT INTO `航标报警分析` VALUES (42, 'C25', '5', '检测航标灯工作高电压报警', NULL, NULL, NULL, NULL, NULL, NULL, NULL, 3, 4, 1440, 1440, NULL, NULL, 'C', NULL, 0, 30);
INSERT INTO `航标报警分析` VALUES (44, 'C31', '9', NULL, NULL, NULL, NULL, NULL, NULL, 30, NULL, 3, 4, 30, 330, NULL, NULL, 'C', NULL, NULL, NULL);
INSERT INTO `航标报警分析` VALUES (45, 'C32', '9', NULL, NULL, NULL, NULL, NULL, 30, NULL, 1, 3, 3, 1440, 1440, NULL, 330, 'A', 'A31', NULL, NULL);
INSERT INTO `航标报警分析` VALUES (47, 'C34', '2', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 3, 4, 330, 330, NULL, NULL, 'C', NULL, 0, 30);
INSERT INTO `航标报警分析` VALUES (49, 'C41', '6', NULL, NULL, 1, NULL, NULL, NULL, 30, NULL, 3, 4, 30, 330, NULL, NULL, 'C', NULL, NULL, NULL);
INSERT INTO `航标报警分析` VALUES (50, 'C42', '6', NULL, NULL, 1, NULL, NULL, 30, NULL, 1, 3, 3, 1440, 1440, NULL, 330, 'A', 'A41', NULL, NULL);
INSERT INTO `航标报警分析` VALUES (52, 'C43', '6', NULL, NULL, 2, NULL, NULL, NULL, NULL, NULL, 3, 3, 1440, 1440, NULL, NULL, 'C', NULL, 0, 30);
INSERT INTO `航标报警分析` VALUES (54, 'C44', '5', '检测终端工作高电压报警', '检测航标灯工作高电压报警', NULL, NULL, NULL, NULL, NULL, NULL, 3, 4, 1440, 1440, NULL, NULL, 'C', NULL, 0, 30);
INSERT INTO `航标报警分析` VALUES (56, 'C45', '1', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 3, 3, 1440, 1440, NULL, NULL, 'C', NULL, 0, 30);

-- ----------------------------
-- Table structure for 航标标签
-- ----------------------------
DROP TABLE IF EXISTS `航标标签`;
CREATE TABLE `航标标签`  (
  `id` int(11) NOT NULL,
  `标签` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of 航标标签
-- ----------------------------
INSERT INTO `航标标签` VALUES (-1, '未打计划内或计划外标签');
INSERT INTO `航标标签` VALUES (0, '未打标签');
INSERT INTO `航标标签` VALUES (1, '专用航标');
INSERT INTO `航标标签` VALUES (2, '锚地');
INSERT INTO `航标标签` VALUES (3, '水工设施');
INSERT INTO `航标标签` VALUES (4, '施工作业');
INSERT INTO `航标标签` VALUES (5, '整治建筑物');
INSERT INTO `航标标签` VALUES (6, '专用航道');
INSERT INTO `航标标签` VALUES (7, '沉船碍航物');
INSERT INTO `航标标签` VALUES (8, '桥区');
INSERT INTO `航标标签` VALUES (9, '一般航标');
INSERT INTO `航标标签` VALUES (10, '重点航标');
INSERT INTO `航标标签` VALUES (11, '计划内');
INSERT INTO `航标标签` VALUES (12, '计划外');
INSERT INTO `航标标签` VALUES (13, '应装');

-- ----------------------------
-- Table structure for 节点信息
-- ----------------------------
DROP TABLE IF EXISTS `节点信息`;
CREATE TABLE `节点信息`  (
  `序号` int(255) NOT NULL,
  `航道里程` double NULL DEFAULT NULL,
  `经度` double NULL DEFAULT NULL,
  `纬度` double NULL DEFAULT NULL,
  `公里数` double NULL DEFAULT NULL,
  PRIMARY KEY (`序号`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = latin1 COLLATE = latin1_swedish_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of 节点信息
-- ----------------------------
INSERT INTO `节点信息` VALUES (1, 160, 113.627687, 29.901661, 0);
INSERT INTO `节点信息` VALUES (2, 159, 113.636363, 29.907532, 1);
INSERT INTO `节点信息` VALUES (3, 158, 113.636363, 29.907599, 2);
INSERT INTO `节点信息` VALUES (4, 157, 113.656178, 29.913853, 3);
INSERT INTO `节点信息` VALUES (5, 156, 113.666001, 29.916463, 4);
INSERT INTO `节点信息` VALUES (6, 155, 113.679387, 29.920843, 5);
INSERT INTO `节点信息` VALUES (7, 154, 113.687984, 29.922775, 6);
INSERT INTO `节点信息` VALUES (8, 153, 113.698195, 29.924219, 7);
INSERT INTO `节点信息` VALUES (9, 152, 113.710924, 29.925259, 8);
INSERT INTO `节点信息` VALUES (10, 151, 113.716661, 29.925107, 9);
INSERT INTO `节点信息` VALUES (11, 150, 113.726829, 29.924463, 10);
INSERT INTO `节点信息` VALUES (12, 149, 113.737295, 29.923284, 11);
INSERT INTO `节点信息` VALUES (13, 148, 113.747667, 29.924151, 12);
INSERT INTO `节点信息` VALUES (14, 147, 113.757869, 29.925448, 13);
INSERT INTO `节点信息` VALUES (15, 146, 113.7682, 29.926693, 14);
INSERT INTO `节点信息` VALUES (16, 145, 113.778693, 29.928162, 15);
INSERT INTO `节点信息` VALUES (17, 144, 113.788648, 29.929521, 16);
INSERT INTO `节点信息` VALUES (18, 143, 113.79883, 29.931258, 17);
INSERT INTO `节点信息` VALUES (19, 142, 113.808857, 29.933972, 18);
INSERT INTO `节点信息` VALUES (20, 141, 113.815119, 29.936465, 19);
INSERT INTO `节点信息` VALUES (21, 140, 113.825039, 29.941265, 20);
INSERT INTO `节点信息` VALUES (22, 139, 113.83211, 29.946979, 21);
INSERT INTO `节点信息` VALUES (23, 138, 113.838579, 29.9541, 22);
INSERT INTO `节点信息` VALUES (24, 137, 113.844115, 29.961676, 23);
INSERT INTO `节点信息` VALUES (25, 136, 113.849281, 29.969426, 24);
INSERT INTO `节点信息` VALUES (26, 135, 113.853934, 29.977172, 25);
INSERT INTO `节点信息` VALUES (27, 134, 113.859078, 29.98549, 26);
INSERT INTO `节点信息` VALUES (28, 133, 113.862442, 29.993997, 27);
INSERT INTO `节点信息` VALUES (29, 132, 113.866844, 30.002023, 28);
INSERT INTO `节点信息` VALUES (30, 131, 113.873765, 30.008848, 29);
INSERT INTO `节点信息` VALUES (31, 130, 113.880557, 30.015086, 30);
INSERT INTO `节点信息` VALUES (32, 129, 113.886848, 30.022118, 31);
INSERT INTO `节点信息` VALUES (33, 128, 113.895015, 30.02773, 32);
INSERT INTO `节点信息` VALUES (34, 127, 113.904006, 30.032225, 33);
INSERT INTO `节点信息` VALUES (35, 126, 113.913541, 30.035855, 34);
INSERT INTO `节点信息` VALUES (36, 125, 113.923303, 30.038703, 35);
INSERT INTO `节点信息` VALUES (37, 124, 113.933095, 30.041618, 36);
INSERT INTO `节点信息` VALUES (38, 123, 113.944481, 30.045062, 37);
INSERT INTO `节点信息` VALUES (39, 122, 113.952512, 30.047976, 38);
INSERT INTO `节点信息` VALUES (40, 121, 113.962117, 30.051224, 39);
INSERT INTO `节点信息` VALUES (41, 120, 113.971504, 30.054538, 40);
INSERT INTO `节点信息` VALUES (42, 119, 113.980893, 30.058062, 41);
INSERT INTO `节点信息` VALUES (43, 118, 113.99027, 30.061881, 42);
INSERT INTO `节点信息` VALUES (44, 117, 113.985277, 30.059796, 43);
INSERT INTO `节点信息` VALUES (45, 116, 114.009481, 30.068696, 44);
INSERT INTO `节点信息` VALUES (46, 115, 114.023159, 30.072738, 45);
INSERT INTO `节点信息` VALUES (47, 114, 114.032724, 30.074772, 46);
INSERT INTO `节点信息` VALUES (48, 113, 114.04275, 30.07723, 47);
INSERT INTO `节点信息` VALUES (49, 112, 114.052268, 30.079286, 48);
INSERT INTO `节点信息` VALUES (50, 111, 114.061574, 30.084475, 49);
INSERT INTO `节点信息` VALUES (51, 110, 114.067937, 30.089001, 50);
INSERT INTO `节点信息` VALUES (52, 109, 114.075507, 30.09481, 51);
INSERT INTO `节点信息` VALUES (53, 108, 114.083246, 30.100993, 52);
INSERT INTO `节点信息` VALUES (54, 107, 114.085227, 30.104511, 53);
INSERT INTO `节点信息` VALUES (55, 106, 114.088863, 30.116856, 54);
INSERT INTO `节点信息` VALUES (56, 105, 114.088223, 30.121842, 55);
INSERT INTO `节点信息` VALUES (57, 104, 114.082279, 30.128749, 56);
INSERT INTO `节点信息` VALUES (58, 103, 114.07356, 30.133783, 57);
INSERT INTO `节点信息` VALUES (59, 102, 114.064901, 30.138726, 58);
INSERT INTO `节点信息` VALUES (60, 101, 114.055583, 30.142831, 59);
INSERT INTO `节点信息` VALUES (61, 100, 114.044911, 30.147615, 60);
INSERT INTO `节点信息` VALUES (62, 99, 114.035719, 30.151969, 61);
INSERT INTO `节点信息` VALUES (63, 98, 114.026341, 30.155924, 62);
INSERT INTO `节点信息` VALUES (64, 97, 114.017083, 30.160059, 63);
INSERT INTO `节点信息` VALUES (65, 96, 114.009045, 30.163787, 64);
INSERT INTO `节点信息` VALUES (66, 95, 114.000087, 30.169486, 65);
INSERT INTO `节点信息` VALUES (67, 94, 113.993076, 30.175688, 66);
INSERT INTO `节点信息` VALUES (68, 93, 113.985975, 30.182279, 67);
INSERT INTO `节点信息` VALUES (69, 92, 113.978365, 30.188841, 68);
INSERT INTO `节点信息` VALUES (70, 91, 113.970545, 30.194713, 69);
INSERT INTO `节点信息` VALUES (71, 90, 113.962544, 30.200311, 70);
INSERT INTO `节点信息` VALUES (72, 89, 113.953669, 30.204952, 71);
INSERT INTO `节点信息` VALUES (73, 88, 113.943572, 30.20654, 72);
INSERT INTO `节点信息` VALUES (74, 87, 113.933007, 30.204363, 73);
INSERT INTO `节点信息` VALUES (75, 86, 113.924067, 30.201147, 74);
INSERT INTO `节点信息` VALUES (76, 85, 113.917779, 30.198584, 75);
INSERT INTO `节点信息` VALUES (77, 84, 113.908262, 30.195021, 76);
INSERT INTO `节点信息` VALUES (78, 83, 113.898884, 30.191216, 77);
INSERT INTO `节点信息` VALUES (79, 82, 113.889147, 30.18798, 78);
INSERT INTO `节点信息` VALUES (80, 81, 113.879139, 30.185793, 79);
INSERT INTO `节点信息` VALUES (81, 80, 113.872555, 30.185483, 80);
INSERT INTO `节点信息` VALUES (82, 79, 113.862271, 30.187681, 81);
INSERT INTO `节点信息` VALUES (83, 78, 113.856279, 30.194692, 82);
INSERT INTO `节点信息` VALUES (84, 77, 113.85574, 30.202961, 83);
INSERT INTO `节点信息` VALUES (85, 76, 113.860593, 30.210902, 84);
INSERT INTO `节点信息` VALUES (86, 75, 113.867281, 30.220191, 85);
INSERT INTO `节点信息` VALUES (87, 74, 113.872555, 30.227861, 86);
INSERT INTO `节点信息` VALUES (88, 73, 113.875563, 30.231815, 87);
INSERT INTO `节点信息` VALUES (89, 72, 113.883401, 30.243201, 88);
INSERT INTO `节点信息` VALUES (90, 71, 113.886697, 30.247785, 89);
INSERT INTO `节点信息` VALUES (91, 70, 113.889393, 30.250751, 90);
INSERT INTO `节点信息` VALUES (92, 69, 113.895865, 30.257762, 91);
INSERT INTO `节点信息` VALUES (93, 68, 113.902217, 30.264893, 92);
INSERT INTO `节点信息` VALUES (94, 67, 113.908269, 30.272174, 93);
INSERT INTO `节点信息` VALUES (95, 66, 113.91474, 30.279185, 94);
INSERT INTO `节点信息` VALUES (96, 65, 113.920115, 30.284854, 95);
INSERT INTO `节点信息` VALUES (97, 64, 113.927227, 30.291362, 96);
INSERT INTO `节点信息` VALUES (98, 63, 113.935616, 30.296605, 97);
INSERT INTO `节点信息` VALUES (99, 62, 113.944669, 30.300536, 98);
INSERT INTO `节点信息` VALUES (100, 61, 113.954454, 30.302906, 99);
INSERT INTO `节点信息` VALUES (101, 60, 113.962102, 30.302508, 100);
INSERT INTO `节点信息` VALUES (102, 59, 113.9716, 30.299691, 101);
INSERT INTO `节点信息` VALUES (103, 58, 113.979592, 30.294017, 102);
INSERT INTO `节点信息` VALUES (104, 57, 113.987287, 30.287883, 103);
INSERT INTO `节点信息` VALUES (105, 56, 113.995117, 30.281966, 104);
INSERT INTO `节点信息` VALUES (106, 55, 114.001852, 30.275674, 105);
INSERT INTO `节点信息` VALUES (107, 54, 114.008098, 30.26845, 106);
INSERT INTO `节点信息` VALUES (108, 53, 114.014074, 30.261622, 107);
INSERT INTO `节点信息` VALUES (109, 52, 114.018755, 30.253112, 108);
INSERT INTO `节点信息` VALUES (110, 51, 114.023061, 30.24579, 109);
INSERT INTO `节点信息` VALUES (111, 50, 114.026572, 30.235792, 110);
INSERT INTO `节点信息` VALUES (112, 49, 114.033669, 30.22916, 111);
INSERT INTO `节点信息` VALUES (113, 48, 114.041656, 30.223716, 112);
INSERT INTO `节点信息` VALUES (114, 47, 114.050618, 30.221216, 113);
INSERT INTO `节点信息` VALUES (115, 46, 114.058373, 30.227254, 114);
INSERT INTO `节点信息` VALUES (116, 45, 114.066232, 30.235389, 115);
INSERT INTO `节点信息` VALUES (117, 44, 114.072312, 30.242656, 116);
INSERT INTO `节点信息` VALUES (118, 43, 114.077869, 30.250283, 117);
INSERT INTO `节点信息` VALUES (119, 42, 114.082473, 30.258345, 118);
INSERT INTO `节点信息` VALUES (120, 41, 114.084359, 30.261798, 119);
INSERT INTO `节点信息` VALUES (121, 40, 114.08743, 30.271141, 120);
INSERT INTO `节点信息` VALUES (122, 39, 114.088701, 30.279997, 121);
INSERT INTO `节点信息` VALUES (123, 38, 114.088722, 30.288972, 122);
INSERT INTO `节点信息` VALUES (124, 37, 114.088362, 30.297935, 123);
INSERT INTO `节点信息` VALUES (125, 36, 114.090565, 30.306387, 124);
INSERT INTO `节点信息` VALUES (126, 35, 114.095166, 30.310277, 125);
INSERT INTO `节点信息` VALUES (127, 34, 114.102832, 30.316683, 126);
INSERT INTO `节点信息` VALUES (128, 33, 114.110057, 30.323209, 127);
INSERT INTO `节点信息` VALUES (129, 32, 114.117048, 30.329903, 128);
INSERT INTO `节点信息` VALUES (130, 31, 114.121104, 30.337955, 129);
INSERT INTO `节点信息` VALUES (131, 30, 114.122488, 30.347861, 130);
INSERT INTO `节点信息` VALUES (132, 29, 114.126866, 30.356281, 131);
INSERT INTO `节点信息` VALUES (133, 28, 114.131972, 30.363866, 132);
INSERT INTO `节点信息` VALUES (134, 27, 114.137989, 30.37145, 133);
INSERT INTO `节点信息` VALUES (135, 26, 114.14933, 30.38287, 134);
INSERT INTO `节点信息` VALUES (136, 25, 114.152162, 30.385411, 135);
INSERT INTO `节点信息` VALUES (137, 24, 114.159344, 30.391979, 136);
INSERT INTO `节点信息` VALUES (138, 23, 114.169147, 30.401246, 137);
INSERT INTO `节点信息` VALUES (139, 22, 114.172585, 30.40575, 138);
INSERT INTO `节点信息` VALUES (140, 21, 114.177543, 30.413631, 139);
INSERT INTO `节点信息` VALUES (141, 20, 114.180936, 30.423914, 140);
INSERT INTO `节点信息` VALUES (142, 19, 114.185047, 30.432536, 141);
INSERT INTO `节点信息` VALUES (143, 18, 114.190301, 30.440247, 142);
INSERT INTO `节点信息` VALUES (144, 17, 114.196572, 30.447408, 143);
INSERT INTO `节点信息` VALUES (145, 16, 114.203329, 30.454271, 144);
INSERT INTO `节点信息` VALUES (146, 15, 114.207874, 30.458771, 145);
INSERT INTO `节点信息` VALUES (147, 14, 114.21287, 30.463806, 146);
INSERT INTO `节点信息` VALUES (148, 13, 114.221454, 30.472981, 147);
INSERT INTO `节点信息` VALUES (149, 12, 114.227595, 30.480291, 148);
INSERT INTO `节点信息` VALUES (150, 11, 114.23351, 30.487698, 149);
INSERT INTO `节点信息` VALUES (151, 10, 114.239744, 30.496283, 150);
INSERT INTO `节点信息` VALUES (152, 9, 114.245479, 30.504029, 151);
INSERT INTO `节点信息` VALUES (153, 8, 114.251493, 30.511431, 152);
INSERT INTO `节点信息` VALUES (154, 7, 114.263106, 30.523833, 153);
INSERT INTO `节点信息` VALUES (155, 6, 114.264593, 30.525346, 154);
INSERT INTO `节点信息` VALUES (156, 5, 114.271082, 30.533059, 155);
INSERT INTO `节点信息` VALUES (157, 4, 114.276377, 30.540874, 156);
INSERT INTO `节点信息` VALUES (158, 3, 114.281159, 30.548794, 157);
INSERT INTO `节点信息` VALUES (159, 2, 114.286104, 30.556768, 158);
INSERT INTO `节点信息` VALUES (160, 1, 114.291887, 30.564214, 159);
INSERT INTO `节点信息` VALUES (161, 0, 114.296667, 30.570289, 160);
INSERT INTO `节点信息` VALUES (162, 1043, 114.298666, 30.572982, 160.2);
INSERT INTO `节点信息` VALUES (163, 1042, 114.304072, 30.580635, 161.2);
INSERT INTO `节点信息` VALUES (164, 1041, 114.309204, 30.588501, 162.2);
INSERT INTO `节点信息` VALUES (165, 1040, 114.314328, 30.596274, 163.2);
INSERT INTO `节点信息` VALUES (166, 1039, 114.319685, 30.604014, 164.2);
INSERT INTO `节点信息` VALUES (167, 1038, 114.326353, 30.610893, 165.2);
INSERT INTO `节点信息` VALUES (168, 1037, 114.333392, 30.61773, 166.2);
INSERT INTO `节点信息` VALUES (169, 1036, 114.340883, 30.623195, 167.2);
INSERT INTO `节点信息` VALUES (170, 1035, 114.348086, 30.62888, 168.2);
INSERT INTO `节点信息` VALUES (171, 1034, 114.35619, 30.634502, 169.2);
INSERT INTO `节点信息` VALUES (172, 1033, 114.364379, 30.640102, 170.2);
INSERT INTO `节点信息` VALUES (173, 1032, 114.372721, 30.645539, 171.2);
INSERT INTO `节点信息` VALUES (174, 1031, 114.381711, 30.650019, 172.2);
INSERT INTO `节点信息` VALUES (175, 1030, 114.394082, 30.655718, 173.2);
INSERT INTO `节点信息` VALUES (176, 1029, 114.403372, 30.658918, 174.2);
INSERT INTO `节点信息` VALUES (177, 1028, 114.413159, 30.662108, 175.2);
INSERT INTO `节点信息` VALUES (178, 1027, 114.423011, 30.665232, 176.2);
INSERT INTO `节点信息` VALUES (179, 1026, 114.43281, 30.668171, 177.2);
INSERT INTO `节点信息` VALUES (180, 1025, 114.440097, 30.670786, 178.2);
INSERT INTO `节点信息` VALUES (181, 1024, 114.449642, 30.673919, 179.2);
INSERT INTO `节点信息` VALUES (182, 1023, 114.459428, 30.677218, 180.2);
INSERT INTO `节点信息` VALUES (183, 1022, 114.470272, 30.680874, 181.2);
INSERT INTO `节点信息` VALUES (184, 1021, 114.479024, 30.683312, 182.2);
INSERT INTO `节点信息` VALUES (185, 1020, 114.487609, 30.68565, 183.2);
INSERT INTO `节点信息` VALUES (186, 1019, 114.497593, 30.687267, 184.2);
INSERT INTO `节点信息` VALUES (187, 1018, 114.50797, 30.686415, 185.2);
INSERT INTO `节点信息` VALUES (188, 1017, 114.518171, 30.684623, 186.2);
INSERT INTO `节点信息` VALUES (189, 1016, 114.526819, 30.681381, 187.2);
INSERT INTO `节点信息` VALUES (190, 1015, 114.536085, 30.673963, 188.2);
INSERT INTO `节点信息` VALUES (191, 1014, 114.542243, 30.666512, 189.2);
INSERT INTO `节点信息` VALUES (192, 1013, 114.546195, 30.658179, 190.2);
INSERT INTO `节点信息` VALUES (193, 1012, 114.550523, 30.649999, 191.2);
INSERT INTO `节点信息` VALUES (194, 1011, 114.55442, 30.641683, 192.2);
INSERT INTO `节点信息` VALUES (195, 1010, 114.557955, 30.633503, 193.2);
INSERT INTO `节点信息` VALUES (196, 1009, 114.562, 30.62496, 194.2);
INSERT INTO `节点信息` VALUES (197, 1008, 114.565204, 30.61648, 195.2);
INSERT INTO `节点信息` VALUES (198, 1007, 114.568104, 30.607779, 196.2);
INSERT INTO `节点信息` VALUES (199, 1006, 114.571162, 30.599194, 197.2);
INSERT INTO `节点信息` VALUES (200, 1005, 114.574199, 30.589881, 198.2);
INSERT INTO `节点信息` VALUES (201, 1004, 114.578441, 30.582297, 199.2);
INSERT INTO `节点信息` VALUES (202, 1003, 114.583466, 30.573879, 200.2);
INSERT INTO `节点信息` VALUES (203, 1002, 114.588081, 30.568978, 201.2);
INSERT INTO `节点信息` VALUES (204, 1001, 114.594902, 30.562588, 202.2);
INSERT INTO `节点信息` VALUES (205, 1000, 114.604064, 30.558952, 203.2);
INSERT INTO `节点信息` VALUES (206, 999, 114.613995, 30.556449, 204.2);
INSERT INTO `节点信息` VALUES (207, 998, 114.624281, 30.555295, 205.2);
INSERT INTO `节点信息` VALUES (208, 997, 114.633623, 30.558708, 206.2);
INSERT INTO `节点信息` VALUES (209, 996, 114.640593, 30.565213, 207.2);
INSERT INTO `节点信息` VALUES (210, 995, 114.648961, 30.570139, 208.2);
INSERT INTO `节点信息` VALUES (211, 994, 114.660178, 30.574849, 209.2);
INSERT INTO `节点信息` VALUES (212, 993, 114.668082, 30.577581, 210.2);
INSERT INTO `节点信息` VALUES (213, 992, 114.677894, 30.58064, 211.2);
INSERT INTO `节点信息` VALUES (214, 991, 114.687864, 30.583337, 212.2);
INSERT INTO `节点信息` VALUES (215, 990, 114.69453, 30.585204, 213.2);
INSERT INTO `节点信息` VALUES (216, 989, 114.704519, 30.58848, 214.2);
INSERT INTO `节点信息` VALUES (217, 988, 114.714217, 30.591947, 215.2);
INSERT INTO `节点信息` VALUES (218, 987, 114.72353, 30.59589, 216.2);
INSERT INTO `节点信息` VALUES (219, 986, 114.732869, 30.600016, 217.2);
INSERT INTO `节点信息` VALUES (220, 985, 114.743134, 30.604253, 218.2);
INSERT INTO `节点信息` VALUES (221, 984, 114.752032, 30.609083, 219.2);
INSERT INTO `节点信息` VALUES (222, 983, 114.761403, 30.611884, 220.2);
INSERT INTO `节点信息` VALUES (223, 982, 114.771934, 30.614223, 221.2);
INSERT INTO `节点信息` VALUES (224, 981, 114.786089, 30.61528, 222.2);
INSERT INTO `节点信息` VALUES (225, 980, 114.793965, 30.613862, 223.2);
INSERT INTO `节点信息` VALUES (226, 979, 114.804636, 30.6113, 224.2);
INSERT INTO `节点信息` VALUES (227, 978, 114.815353, 30.60774, 225.2);
INSERT INTO `节点信息` VALUES (228, 977, 114.823205, 30.603233, 226.2);
INSERT INTO `节点信息` VALUES (229, 976, 114.831016, 30.597299, 227.2);
INSERT INTO `节点信息` VALUES (230, 975, 114.835612, 30.592962, 228.2);
INSERT INTO `节点信息` VALUES (231, 974, 114.836983, 30.590316, 229.2);
INSERT INTO `节点信息` VALUES (232, 973, 114.838137, 30.588028, 230.2);
INSERT INTO `节点信息` VALUES (233, 972, 114.839514, 30.585194, 231.2);
INSERT INTO `节点信息` VALUES (234, 971, 114.840769, 30.582703, 232.2);
INSERT INTO `节点信息` VALUES (235, 970, 114.841529, 30.580693, 233.2);
INSERT INTO `节点信息` VALUES (236, 969, 114.841915, 30.578906, 234.2);
INSERT INTO `节点信息` VALUES (237, 968, 114.841757, 30.577413, 235.2);
INSERT INTO `节点信息` VALUES (238, 967, 114.841571, 30.56853, 236.2);
INSERT INTO `节点信息` VALUES (239, 966, 114.838755, 30.559846, 237.2);
INSERT INTO `节点信息` VALUES (240, 965, 114.838748, 30.559552, 238.2);
INSERT INTO `节点信息` VALUES (241, 964, 114.835019, 30.542073, 239.2);
INSERT INTO `节点信息` VALUES (242, 963, 114.833478, 30.533129, 240.2);
INSERT INTO `节点信息` VALUES (243, 962, 114.831679, 30.524317, 241.2);
INSERT INTO `节点信息` VALUES (244, 961, 114.830313, 30.515377, 242.2);
INSERT INTO `节点信息` VALUES (245, 960, 114.828866, 30.505606, 243.2);
INSERT INTO `节点信息` VALUES (246, 959, 114.827709, 30.496894, 244.2);
INSERT INTO `节点信息` VALUES (247, 958, 114.82673, 30.487917, 245.2);
INSERT INTO `节点信息` VALUES (248, 957, 114.826634, 30.478937, 246.2);
INSERT INTO `节点信息` VALUES (249, 956, 114.825692, 30.469958, 247.2);
INSERT INTO `节点信息` VALUES (250, 955, 114.825459, 30.459826, 248.2);
INSERT INTO `节点信息` VALUES (251, 954, 114.825831, 30.451097, 249.2);
INSERT INTO `节点信息` VALUES (252, 953, 114.82695, 30.442886, 250.2);
INSERT INTO `节点信息` VALUES (253, 952, 114.833298, 30.433704, 251.2);
INSERT INTO `节点信息` VALUES (254, 951, 114.846773, 30.427421, 252.2);
INSERT INTO `节点信息` VALUES (255, 950, 114.856763, 30.424035, 253.2);
INSERT INTO `节点信息` VALUES (256, 949, 114.866457, 30.421215, 254.2);
INSERT INTO `节点信息` VALUES (257, 948, 114.876362, 30.418655, 255.2);
INSERT INTO `节点信息` VALUES (258, 947, 114.886833, 30.416089, 256.2);
INSERT INTO `节点信息` VALUES (259, 946, 114.896762, 30.415217, 257.2);
INSERT INTO `节点信息` VALUES (260, 945, 114.90879, 30.413963, 258.2);
INSERT INTO `节点信息` VALUES (261, 944, 114.919004, 30.413078, 259.2);
INSERT INTO `节点信息` VALUES (262, 943, 114.929359, 30.412107, 260.2);
INSERT INTO `节点信息` VALUES (263, 942, 114.939737, 30.411112, 261.2);
INSERT INTO `节点信息` VALUES (264, 941, 114.950092, 30.410401, 262.2);
INSERT INTO `节点信息` VALUES (265, 940, 114.958443, 30.409988, 263.2);
INSERT INTO `节点信息` VALUES (266, 939, 114.968716, 30.40924, 264.2);
INSERT INTO `节点信息` VALUES (267, 938, 114.979141, 30.408197, 265.2);
INSERT INTO `节点信息` VALUES (268, 937, 114.988998, 30.405496, 266.2);
INSERT INTO `节点信息` VALUES (269, 936, 114.999092, 30.403672, 267.2);
INSERT INTO `节点信息` VALUES (270, 935, 115.011561, 30.403062, 268.2);
INSERT INTO `节点信息` VALUES (271, 934, 115.021776, 30.402203, 269.2);
INSERT INTO `节点信息` VALUES (272, 933, 115.031657, 30.399147, 270.2);
INSERT INTO `节点信息` VALUES (273, 932, 115.04078, 30.39481, 271.2);
INSERT INTO `节点信息` VALUES (274, 931, 115.049989, 30.390114, 272.2);
INSERT INTO `节点信息` VALUES (275, 930, 115.057754, 30.382287, 273.2);
INSERT INTO `节点信息` VALUES (276, 929, 115.063423, 30.375213, 274.2);
INSERT INTO `节点信息` VALUES (277, 928, 115.068919, 30.367539, 275.2);
INSERT INTO `节点信息` VALUES (278, 927, 115.074179, 30.359798, 276.2);
INSERT INTO `节点信息` VALUES (279, 926, 115.078822, 30.351781, 277.2);
INSERT INTO `节点信息` VALUES (280, 925, 115.08379, 30.339742, 278.2);
INSERT INTO `节点信息` VALUES (281, 924, 115.085746, 30.330678, 279.2);
INSERT INTO `节点信息` VALUES (282, 923, 115.086835, 30.321742, 280.2);
INSERT INTO `节点信息` VALUES (283, 922, 115.087436, 30.312774, 281.2);
INSERT INTO `节点信息` VALUES (284, 921, 115.087586, 30.303801, 282.2);
INSERT INTO `节点信息` VALUES (285, 920, 115.086793, 30.297265, 283.2);
INSERT INTO `节点信息` VALUES (286, 919, 115.084503, 30.288899, 284.2);
INSERT INTO `节点信息` VALUES (287, 918, 115.081049, 30.280452, 285.2);
INSERT INTO `节点信息` VALUES (288, 917, 115.076203, 30.26825, 286.2);
INSERT INTO `节点信息` VALUES (289, 916, 115.074816, 30.263306, 287.2);
INSERT INTO `节点信息` VALUES (290, 915, 115.073836, 30.253881, 288.2);
INSERT INTO `节点信息` VALUES (291, 914, 115.073164, 30.245191, 289.2);
INSERT INTO `节点信息` VALUES (292, 913, 115.074733, 30.236395, 290.2);
INSERT INTO `节点信息` VALUES (293, 912, 115.081435, 30.229637, 291.2);
INSERT INTO `节点信息` VALUES (294, 911, 115.089151, 30.223724, 292.2);
INSERT INTO `节点信息` VALUES (295, 910, 115.095306, 30.219927, 293.2);
INSERT INTO `节点信息` VALUES (296, 909, 115.104399, 30.216271, 294.2);
INSERT INTO `节点信息` VALUES (297, 908, 115.114311, 30.213596, 295.2);
INSERT INTO `节点信息` VALUES (298, 907, 115.12453, 30.212225, 296.2);
INSERT INTO `节点信息` VALUES (299, 906, 115.134937, 30.211428, 297.2);
INSERT INTO `节点信息` VALUES (300, 905, 115.142782, 30.211001, 298.2);
INSERT INTO `节点信息` VALUES (301, 904, 115.15222, 30.213362, 299.2);
INSERT INTO `节点信息` VALUES (302, 903, 115.161362, 30.217426, 300.2);
INSERT INTO `节点信息` VALUES (303, 902, 115.171417, 30.219705, 301.2);
INSERT INTO `节点信息` VALUES (304, 901, 115.181682, 30.221123, 302.2);
INSERT INTO `节点信息` VALUES (305, 900, 115.190295, 30.221333, 303.2);
INSERT INTO `节点信息` VALUES (306, 899, 115.200193, 30.218633, 304.2);
INSERT INTO `节点信息` VALUES (307, 898, 115.209387, 30.214649, 305.2);
INSERT INTO `节点信息` VALUES (308, 897, 115.217424, 30.208518, 306.2);
INSERT INTO `节点信息` VALUES (309, 896, 115.222807, 30.201229, 307.2);
INSERT INTO `节点信息` VALUES (310, 895, 115.229133, 30.193708, 308.2);
INSERT INTO `节点信息` VALUES (311, 894, 115.235715, 30.186292, 309.2);
INSERT INTO `节点信息` VALUES (312, 893, 115.242198, 30.179229, 310.2);
INSERT INTO `节点信息` VALUES (313, 892, 115.248595, 30.172142, 311.2);
INSERT INTO `节点信息` VALUES (314, 891, 115.255146, 30.165171, 312.2);
INSERT INTO `节点信息` VALUES (315, 890, 115.261045, 30.158705, 313.2);
INSERT INTO `节点信息` VALUES (316, 889, 115.267431, 30.151634, 314.2);
INSERT INTO `节点信息` VALUES (317, 888, 115.273634, 30.144747, 315.2);
INSERT INTO `节点信息` VALUES (318, 887, 115.280509, 30.137693, 316.2);
INSERT INTO `节点信息` VALUES (319, 886, 115.286545, 30.130369, 317.2);
INSERT INTO `节点信息` VALUES (320, 885, 115.291813, 30.123752, 318.2);
INSERT INTO `节点信息` VALUES (321, 884, 115.297891, 30.116024, 319.2);
INSERT INTO `节点信息` VALUES (322, 883, 115.303674, 30.108619, 320.2);
INSERT INTO `节点信息` VALUES (323, 882, 115.309305, 30.100973, 321.2);
INSERT INTO `节点信息` VALUES (324, 881, 115.314782, 30.093349, 322.2);
INSERT INTO `节点信息` VALUES (325, 880, 115.321036, 30.083505, 323.2);
INSERT INTO `节点信息` VALUES (326, 879, 115.324939, 30.074939, 324.2);
INSERT INTO `节点信息` VALUES (327, 878, 115.326412, 30.066041, 325.2);
INSERT INTO `节点信息` VALUES (328, 877, 115.325162, 30.057179, 326.2);
INSERT INTO `节点信息` VALUES (329, 876, 115.32349, 30.048368, 327.2);
INSERT INTO `节点信息` VALUES (330, 875, 115.322962, 30.044138, 328.2);
INSERT INTO `节点信息` VALUES (331, 874, 115.32435, 30.035505, 329.2);
INSERT INTO `节点信息` VALUES (332, 873, 115.3277, 30.02662, 330.2);
INSERT INTO `节点信息` VALUES (333, 872, 115.330455, 30.022435, 331.2);
INSERT INTO `节点信息` VALUES (334, 871, 115.340956, 30.013673, 332.2);
INSERT INTO `节点信息` VALUES (335, 870, 115.349572, 30.007694, 333.2);
INSERT INTO `节点信息` VALUES (336, 869, 115.357401, 30.002115, 334.2);
INSERT INTO `节点信息` VALUES (337, 868, 115.362434, 29.994436, 335.2);
INSERT INTO `节点信息` VALUES (338, 867, 115.36736, 29.986557, 336.2);
INSERT INTO `节点信息` VALUES (339, 866, 115.372137, 29.978509, 337.2);
INSERT INTO `节点信息` VALUES (340, 865, 115.378192, 29.970564, 338.2);
INSERT INTO `节点信息` VALUES (341, 864, 115.38534, 29.964338, 339.2);
INSERT INTO `节点信息` VALUES (342, 863, 115.393049, 29.958286, 340.2);
INSERT INTO `节点信息` VALUES (343, 862, 115.39968, 29.952114, 341.2);
INSERT INTO `节点信息` VALUES (344, 861, 115.405116, 29.943853, 342.2);
INSERT INTO `节点信息` VALUES (345, 860, 115.404806, 29.933998, 343.2);
INSERT INTO `节点信息` VALUES (346, 859, 115.403691, 29.925126, 344.2);
INSERT INTO `节点信息` VALUES (347, 858, 115.40696, 29.916651, 345.2);
INSERT INTO `节点信息` VALUES (348, 857, 115.411928, 29.909029, 346.2);
INSERT INTO `节点信息` VALUES (349, 856, 115.419886, 29.904451, 347.2);
INSERT INTO `节点信息` VALUES (350, 855, 115.426908, 29.89935, 348.2);
INSERT INTO `节点信息` VALUES (351, 854, 115.433128, 29.892657, 349.2);
INSERT INTO `节点信息` VALUES (352, 853, 115.439565, 29.885535, 350.2);
INSERT INTO `节点信息` VALUES (353, 852, 115.445566, 29.878222, 351.2);
INSERT INTO `节点信息` VALUES (354, 851, 115.45204, 29.87116, 352.2);
INSERT INTO `节点信息` VALUES (355, 850, 115.45723, 29.864056, 353.2);
INSERT INTO `节点信息` VALUES (356, 849, 115.46527, 29.857965, 354.2);
INSERT INTO `节点信息` VALUES (357, 848, 115.472952, 29.851926, 355.2);
INSERT INTO `节点信息` VALUES (358, 847, 115.481701, 29.847333, 356.2);
INSERT INTO `节点信息` VALUES (359, 846, 115.491509, 29.84418, 357.2);
INSERT INTO `节点信息` VALUES (360, 845, 115.498671, 29.842675, 358.2);
INSERT INTO `节点信息` VALUES (361, 844, 115.510352, 29.840115, 359.2);
INSERT INTO `节点信息` VALUES (362, 843, 115.518804, 29.838846, 360.2);
INSERT INTO `节点信息` VALUES (363, 842, 115.529043, 29.837728, 361.2);
INSERT INTO `节点信息` VALUES (364, 841, 115.539389, 29.837491, 362.2);
INSERT INTO `节点信息` VALUES (365, 840, 115.550674, 29.837046, 363.2);
INSERT INTO `节点信息` VALUES (366, 839, 115.561045, 29.836967, 364.2);
INSERT INTO `节点信息` VALUES (367, 838, 115.571348, 29.837634, 365.2);
INSERT INTO `节点信息` VALUES (368, 837, 115.581608, 29.837913, 366.2);
INSERT INTO `节点信息` VALUES (369, 836, 115.592105, 29.837913, 367.2);
INSERT INTO `节点信息` VALUES (370, 835, 115.601957, 29.838359, 368.2);
INSERT INTO `节点信息` VALUES (371, 834, 115.612284, 29.839023, 369.2);
INSERT INTO `节点信息` VALUES (372, 833, 115.622566, 29.839905, 370.2);
INSERT INTO `节点信息` VALUES (373, 832, 115.632817, 29.841335, 371.2);
INSERT INTO `节点信息` VALUES (374, 831, 115.643038, 29.843008, 372.2);
INSERT INTO `节点信息` VALUES (375, 830, 115.650496, 29.844701, 373.2);

-- ----------------------------
-- Table structure for 调度分析
-- ----------------------------
DROP TABLE IF EXISTS `调度分析`;
CREATE TABLE `调度分析`  (
  `序号` int(11) NOT NULL,
  `异常编号` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `调度阶段` int(11) NULL DEFAULT NULL,
  `最早调度时限` float NULL DEFAULT NULL,
  `最晚调度时限` float NULL DEFAULT NULL,
  `参照编号` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `定级建议` int(11) NULL DEFAULT NULL,
  `分类建议` int(11) NULL DEFAULT NULL,
  `调度要求` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`序号`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of 调度分析
-- ----------------------------
INSERT INTO `调度分析` VALUES (1, 'A11', 1, 0, 30, NULL, 1, 1, '一类');
INSERT INTO `调度分析` VALUES (2, 'A11', 99, 30, 9999, NULL, 1, 1, '一类');
INSERT INTO `调度分析` VALUES (3, 'A12', 1, 0, 30, NULL, 1, 1, '一类');
INSERT INTO `调度分析` VALUES (4, 'A12', 99, 30, 9999, NULL, 1, 1, '一类');
INSERT INTO `调度分析` VALUES (5, 'A13', 1, 0, 30, NULL, 2, 2, '二类');
INSERT INTO `调度分析` VALUES (6, 'A13', 2, 30, 180, NULL, 1, 1, '一类');
INSERT INTO `调度分析` VALUES (7, 'A13', 99, 180, 9999, NULL, 1, 1, '一类');
INSERT INTO `调度分析` VALUES (8, 'A21', 1, 0, 30, NULL, 3, 4, '四类');
INSERT INTO `调度分析` VALUES (9, 'A21', 2, 30, 60, NULL, 1, 1, '一类');
INSERT INTO `调度分析` VALUES (10, 'A21', 99, 60, 9999, NULL, 1, 1, '一类');
INSERT INTO `调度分析` VALUES (11, 'A22', 1, 0, 30, NULL, 3, 4, '四类');
INSERT INTO `调度分析` VALUES (12, 'A22', 2, 30, 60, NULL, 2, 2, '二类');
INSERT INTO `调度分析` VALUES (13, 'A22', 3, 60, 180, NULL, 1, 1, '一类');
INSERT INTO `调度分析` VALUES (14, 'A22', 99, 180, 9999, NULL, 1, 1, '一类');
INSERT INTO `调度分析` VALUES (15, 'A31', 1, 0, 30, NULL, 3, 4, '四类');
INSERT INTO `调度分析` VALUES (16, 'A31', 2, 30, 60, NULL, 2, 2, '二类');
INSERT INTO `调度分析` VALUES (17, 'A31', 3, 60, 180, NULL, 1, 1, '一类');
INSERT INTO `调度分析` VALUES (18, 'A31', 99, 180, 9999, NULL, 1, 1, '一类');
INSERT INTO `调度分析` VALUES (19, 'A41', 1, 0, 30, NULL, 3, 4, '四类');
INSERT INTO `调度分析` VALUES (20, 'A41', 2, 30, 60, NULL, 2, 2, '二类');
INSERT INTO `调度分析` VALUES (21, 'A41', 3, 60, 180, NULL, 1, 1, '一类');
INSERT INTO `调度分析` VALUES (22, 'A41', 99, 180, 9999, NULL, 1, 1, '一类');
INSERT INTO `调度分析` VALUES (23, 'B11', 1, 0, 30, NULL, 2, 2, '二类');
INSERT INTO `调度分析` VALUES (24, 'B21', 1, 0, 30, NULL, 3, 4, '四类');
INSERT INTO `调度分析` VALUES (25, 'B21', 2, 30, 60, NULL, 2, 2, '二类');
INSERT INTO `调度分析` VALUES (26, 'B21', 99, 60, 9999, NULL, 1, 1, '一类');
INSERT INTO `调度分析` VALUES (27, 'B22', 1, 0, 30, NULL, 3, 4, '四类');
INSERT INTO `调度分析` VALUES (28, 'B22', 2, 30, 60, NULL, 2, 2, '二类');
INSERT INTO `调度分析` VALUES (29, 'B23', 1, 0, 30, NULL, 2, 3, '三类');
INSERT INTO `调度分析` VALUES (30, 'B23', 99, 30, 9999, NULL, 1, 1, '一类');
INSERT INTO `调度分析` VALUES (31, 'B31', 1, 0, 30, NULL, 3, 4, '四类');
INSERT INTO `调度分析` VALUES (32, 'B31', 2, 30, 60, NULL, 2, 2, '二类');
INSERT INTO `调度分析` VALUES (33, 'B41', 1, 0, 30, NULL, 3, 4, '四类');
INSERT INTO `调度分析` VALUES (34, 'B41', 2, 30, 60, NULL, 2, 2, '二类');
INSERT INTO `调度分析` VALUES (35, 'B42', 1, 0, 30, NULL, 2, 3, '三类');
INSERT INTO `调度分析` VALUES (36, 'B42', 99, 30, 9999, NULL, 1, 1, '一类');
INSERT INTO `调度分析` VALUES (37, 'C11', 1, 0, 30, NULL, 3, 3, '三类');
INSERT INTO `调度分析` VALUES (38, 'C11', 99, 30, 9999, NULL, 1, 1, '一类');
INSERT INTO `调度分析` VALUES (39, 'C12', 1, 0, 30, NULL, 3, 4, '基点');
INSERT INTO `调度分析` VALUES (40, 'C12', 99, 30, 9999, NULL, 1, 1, '一类');
INSERT INTO `调度分析` VALUES (41, 'C13', 1, 0, 30, NULL, 2, 2, '二类');
INSERT INTO `调度分析` VALUES (42, 'C13', 2, 150, 180, NULL, 3, 4, '基点');
INSERT INTO `调度分析` VALUES (43, 'C13', 99, 180, 9999, NULL, 1, 1, '一类');
INSERT INTO `调度分析` VALUES (44, 'C21', 1, 0, 30, NULL, 3, 4, '四类');
INSERT INTO `调度分析` VALUES (45, 'C22', 1, 0, 30, NULL, 3, 4, '四类');
INSERT INTO `调度分析` VALUES (46, 'C23', 1, 0, 30, NULL, 3, 4, '四类');
INSERT INTO `调度分析` VALUES (47, 'C24', 1, 0, 30, NULL, 3, 4, '四类');
INSERT INTO `调度分析` VALUES (48, 'C24', 2, 30, 60, NULL, 2, 2, '二类');
INSERT INTO `调度分析` VALUES (49, 'C24', 3, 60, 150, NULL, 3, 3, '三类');
INSERT INTO `调度分析` VALUES (50, 'C24', 99, 150, 9999, NULL, 1, 1, '一类');
INSERT INTO `调度分析` VALUES (51, 'C25', 1, 0, 30, NULL, 3, 4, '四类');
INSERT INTO `调度分析` VALUES (52, 'C25', 99, 30, 9999, NULL, 1, 1, '一类');
INSERT INTO `调度分析` VALUES (53, 'C31', 1, 0, 30, NULL, 3, 4, '四类');
INSERT INTO `调度分析` VALUES (54, 'C32', 1, 0, 30, NULL, 3, 4, '四类');
INSERT INTO `调度分析` VALUES (55, 'C32', 2, 30, 60, NULL, 2, 2, '二类');
INSERT INTO `调度分析` VALUES (56, 'C32', 3, 60, 150, NULL, 3, 3, '三类');
INSERT INTO `调度分析` VALUES (57, 'C32', 99, 150, 9999, NULL, 1, 1, '一类');
INSERT INTO `调度分析` VALUES (58, 'C34', 1, 0, 30, NULL, 3, 4, '四类');
INSERT INTO `调度分析` VALUES (59, 'C34', 99, 30, 9999, NULL, 1, 1, '一类');
INSERT INTO `调度分析` VALUES (60, 'C41', 1, 0, 30, NULL, 3, 4, '四类');
INSERT INTO `调度分析` VALUES (61, 'C42', 1, 0, 30, NULL, 3, 4, '四类');
INSERT INTO `调度分析` VALUES (62, 'C42', 2, 30, 60, NULL, 2, 2, '二类');
INSERT INTO `调度分析` VALUES (63, 'C42', 3, 60, 150, NULL, 3, 3, '三类');
INSERT INTO `调度分析` VALUES (64, 'C42', 99, 150, 9999, NULL, 1, 1, '一类');
INSERT INTO `调度分析` VALUES (65, 'C43', 1, 0, 30, NULL, 3, 3, '三类');
INSERT INTO `调度分析` VALUES (66, 'C43', 99, 30, 9999, NULL, 1, 1, '一类');
INSERT INTO `调度分析` VALUES (67, 'C44', 1, 0, 30, NULL, 3, 4, '四类');
INSERT INTO `调度分析` VALUES (68, 'C44', 99, 30, 9999, NULL, 1, 1, '一类');
INSERT INTO `调度分析` VALUES (69, 'C45', 1, 0, 30, NULL, 3, 3, '三类');
INSERT INTO `调度分析` VALUES (70, 'C45', 99, 30, 9999, NULL, 1, 1, '一类');
INSERT INTO `调度分析` VALUES (101, 'CK1', 1, 0, 30, NULL, 3, 4, '四类');
INSERT INTO `调度分析` VALUES (102, 'CK2', 2, 30, 60, NULL, 2, 2, '二类');
INSERT INTO `调度分析` VALUES (103, 'CK3', 3, 60, 150, NULL, 3, 3, '三类');
INSERT INTO `调度分析` VALUES (104, 'CK3', 99, 150, 9999, NULL, 1, 1, '一类');

-- ----------------------------
-- Table structure for 重点航标清单
-- ----------------------------
DROP TABLE IF EXISTS `重点航标清单`;
CREATE TABLE `重点航标清单`  (
  `序号` int(11) NOT NULL,
  `航标` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`序号`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of 重点航标清单
-- ----------------------------
INSERT INTO `重点航标清单` VALUES (1, '天兴洲桥#1白浮');
INSERT INTO `重点航标清单` VALUES (2, '天兴洲桥#1红浮');
INSERT INTO `重点航标清单` VALUES (3, '天兴洲桥#2白浮');
INSERT INTO `重点航标清单` VALUES (4, '天兴洲桥#2红浮');
INSERT INTO `重点航标清单` VALUES (5, '武汉二桥#1白浮');
INSERT INTO `重点航标清单` VALUES (6, '武汉二桥#1红浮');
INSERT INTO `重点航标清单` VALUES (7, '武汉二桥#2白浮');
INSERT INTO `重点航标清单` VALUES (8, '武汉二桥#2红浮');
INSERT INTO `重点航标清单` VALUES (9, '武桥上水#1白浮');
INSERT INTO `重点航标清单` VALUES (10, '武桥上水#2白浮');
INSERT INTO `重点航标清单` VALUES (11, '武桥下水#1白浮');
INSERT INTO `重点航标清单` VALUES (12, '武桥下水#1红浮');
INSERT INTO `重点航标清单` VALUES (13, '武桥下水#2白浮');
INSERT INTO `重点航标清单` VALUES (14, '武桥下水#2红浮');
INSERT INTO `重点航标清单` VALUES (15, '嘉鱼岩#1红浮');
INSERT INTO `重点航标清单` VALUES (16, '嘉鱼岩#2红浮');
INSERT INTO `重点航标清单` VALUES (17, '黄石头礁石#2红浮');
INSERT INTO `重点航标清单` VALUES (18, '金口列礁#2红浮');
INSERT INTO `重点航标清单` VALUES (19, '军山桥#1白浮');
INSERT INTO `重点航标清单` VALUES (20, '军山桥#1红浮');
INSERT INTO `重点航标清单` VALUES (21, '军山桥#2白浮');
INSERT INTO `重点航标清单` VALUES (22, '军山桥#2红浮');
INSERT INTO `重点航标清单` VALUES (23, '鄂州电厂#1红浮');
INSERT INTO `重点航标清单` VALUES (24, '猴子矶#1红浮');
INSERT INTO `重点航标清单` VALUES (25, '猴子矶#2红浮');
INSERT INTO `重点航标清单` VALUES (26, '美利石红浮');
INSERT INTO `重点航标清单` VALUES (27, '黄冈桥#2白浮');
INSERT INTO `重点航标清单` VALUES (28, '黄冈桥#2红浮');
INSERT INTO `重点航标清单` VALUES (29, '搁排矶白浮');
INSERT INTO `重点航标清单` VALUES (30, '搁排矶危险水域浮');
INSERT INTO `重点航标清单` VALUES (31, '观音阁红浮');
INSERT INTO `重点航标清单` VALUES (32, '猴儿矶红浮');
INSERT INTO `重点航标清单` VALUES (33, '黄石桥#1左右通航浮');
INSERT INTO `重点航标清单` VALUES (34, '黄石桥#2左右通航浮');
INSERT INTO `重点航标清单` VALUES (35, '黄石桥上水#1白浮');
INSERT INTO `重点航标清单` VALUES (36, '黄石桥上水#2白浮');
INSERT INTO `重点航标清单` VALUES (37, '黄石桥上水#3白浮');
INSERT INTO `重点航标清单` VALUES (38, '黄石桥下水#1红浮');
INSERT INTO `重点航标清单` VALUES (39, '黄石桥下水#2红浮');
INSERT INTO `重点航标清单` VALUES (40, '黄石礁#1红浮');
INSERT INTO `重点航标清单` VALUES (41, '黄石礁#2红浮');
INSERT INTO `重点航标清单` VALUES (42, '蕲河口沉船白浮');
INSERT INTO `重点航标清单` VALUES (43, '洞庭礁红浮');
INSERT INTO `重点航标清单` VALUES (44, '黄石头礁石#1红浮');
INSERT INTO `重点航标清单` VALUES (45, '金口列礁#1红浮');

-- ----------------------------
-- Table structure for 阈值特批清单
-- ----------------------------
DROP TABLE IF EXISTS `阈值特批清单`;
CREATE TABLE `阈值特批清单`  (
  `航标` varchar(50) CHARACTER SET gbk COLLATE gbk_chinese_ci NULL DEFAULT NULL,
  `理论位移阈值` varchar(10) CHARACTER SET gbk COLLATE gbk_chinese_ci NULL DEFAULT NULL,
  `理论漂移阈值` varchar(10) CHARACTER SET gbk COLLATE gbk_chinese_ci NULL DEFAULT NULL,
  `时期` varchar(10) CHARACTER SET gbk COLLATE gbk_chinese_ci NULL DEFAULT NULL
) ENGINE = InnoDB CHARACTER SET = gbk COLLATE = gbk_chinese_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of 阈值特批清单
-- ----------------------------
INSERT INTO `阈值特批清单` VALUES ('xxx浮标', '80', '150', '非汛期');

-- ----------------------------
-- Table structure for 阈值规定
-- ----------------------------
DROP TABLE IF EXISTS `阈值规定`;
CREATE TABLE `阈值规定`  (
  `理论位移阈值` int(10) NULL DEFAULT NULL,
  `理论漂移阈值` int(10) NULL DEFAULT NULL,
  `时期` varchar(10) CHARACTER SET gbk COLLATE gbk_chinese_ci NULL DEFAULT NULL,
  `航标重要程度` varchar(10) CHARACTER SET gbk COLLATE gbk_chinese_ci NULL DEFAULT NULL,
  `航标类型` varchar(10) CHARACTER SET gbk COLLATE gbk_chinese_ci NULL DEFAULT NULL,
  `理论日光阈值` int(10) NULL DEFAULT NULL,
  `理论轮询周期` int(10) NULL DEFAULT NULL,
  `理论报警周期` int(10) NULL DEFAULT NULL
) ENGINE = InnoDB CHARACTER SET = gbk COLLATE = gbk_chinese_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of 阈值规定
-- ----------------------------
INSERT INTO `阈值规定` VALUES (40, 100, '汛期', '重点', '浮标', 208, 60, 10);
INSERT INTO `阈值规定` VALUES (50, 100, '汛期', '一般', '浮标', 208, NULL, NULL);
INSERT INTO `阈值规定` VALUES (30, 100, '非汛期', '一般', '浮标', 208, 60, 10);
INSERT INTO `阈值规定` VALUES (20, 100, '非汛期', '重点', '浮标', 208, 60, 10);
INSERT INTO `阈值规定` VALUES (50, 100, NULL, NULL, '岸标', 208, 60, 10);

-- ----------------------------
-- Function structure for 机构排序
-- ----------------------------
DROP FUNCTION IF EXISTS `机构排序`;
delimiter ;;
CREATE FUNCTION `机构排序`(单位 VARCHAR(50) CHARACTER SET utf8mb4)
 RETURNS int(11)
BEGIN
		return (select 序号 from `基层处` where 基层处.单位=单位);
END
;;
delimiter ;

-- ----------------------------
-- Function structure for 水位站排序
-- ----------------------------
DROP FUNCTION IF EXISTS `水位站排序`;
delimiter ;;
CREATE FUNCTION `水位站排序`(站点名称 VARCHAR(50) CHARACTER SET utf8mb4)
 RETURNS int(11)
BEGIN
		return (select 序号 from `水位站` where 水位站.站点名称=站点名称);
END
;;
delimiter ;

SET FOREIGN_KEY_CHECKS = 1;
