# -*- coding: utf-8 -*-
# PDT列表
PDTList = ['U2000-T', 'U2000-B', 'U2000-IP', 'U2000-I', 'uTraffic', 'UEasy', 'NetMatrix', 'N2510', 'iBridge', 'NetOpen',
           'ICTO-SDN', 'AC-Campus', 'AC-DCN', 'AC-WAN', 'T-SDN', 'AC-Branch','TMS1000',
           'Agile_Controller-Super', 'CloudOpera_Orchestrator_SDN', 'NCE-Super(V1R17C10)', 'NCE-IP', 'NCE-T',
           'NCE-Analysis', 'NCE-Super']
# PDT对应的SPU列表
SPUList = {'U2000-T':'NCE-T',
           'U2000-B':'NCE-FAN',
           'U2000-IP':'NCE-IP',
           'U2000-I':'NCE-Common',
           'uTraffic':'NCE-分析',
           'UEasy':'NA',
           'NetMatrix':'NA',
           'N2510':'NCE-FAN',
           'iBridge':'NA',
           'NetOpen':'NCE-FAN',
           'ICTO-SDN':'NCE-FAN',
           'AC-Campus':'NCE-E/Campus',
           'AC-DCN':'NCE-E/DCN',
           'AC-WAN':'NCE-IP',
           'T-SDN':'NA',
           'AC-Branch':'NA',
           'TMS1000':'NCE-FAN',
           'Agile_Controller-Super':'NCE-Super',
           'CloudOpera_Orchestrator_SDN':'NA',
           'NCE-Super(V1R17C10)':'NCE-Super',
           'NCE-IP':'NCE-IP',
           'NCE-T':'NCE-T',
           'NCE-Analysis':'NCE-分析',
           'NCE-Super':'NCE-Super'
           }

# 开发部和对应的特性
DeptList = {
    '平台': ['imap平台', 'iWeb平台', 'iMap平台License', 'TOMCAT', '工程平台UniEP', 'uTraffic-平台OSS3.0', 'uTraffic-平台cloudsop',
           'CloudSOP(业务)', 'CloudSOP(UniEP)', 'PaaS'],
    '工程': ['工程安装框架', '升级/补丁框架', '工程维护工具', '工程双机', 'DB', 'OS', 'Veritas'],
    '传送': ['SDH E2E路径创建', '告警框架', 'PTN界面', '数据业务', '传送VRP-其他', 'OTN-其他', 'SDH E2E路径搜索', 'RTN配置',
           'PTN配置', 'WDM E2E路径管理', '智能-其他', 'MSTP业务', '数据配置', 'SDH智能', 'ETH E2E路径创建',
           '传送VRP-分组特性', '界面公共', '网元通信', '传送VRP-框架', 'RTN-其他', '传送VRP-告警', 'ETH E2E路径搜索',
           'WDM E2E路径搜索', '网元安全管理', 'MML远维', '海缆', '波分', 'ETH E2E路径管理', '分布式框架', '传送TCAT',
           'ETH E2E-其他', '持久层框架', '传送VRP-通用配置', '波分智能', '数据WebLCT', '核心配置-其它', '性能框架',
           '网元迁移', 'WebLCT公共', 'WDM E2E-其他', 'OTN配置', '进程框架', '传送VRP-性能', '微波WebLCT',
           '传送VRP-网元通讯', '基本配置', 'SDH E2E-其他', '传送工程/升级', 'WDM E2E保护子网', '波分WebLCT', 'mirror db',
           'MSTP-其他', 'Adapter框架', '数据 -其他', '传送VRP -SDH特性', '脚本导入导出框架', 'MSTP配置', '传送License',
           'PTN业务', '传送VRP-波分特性', 'OTN业务', 'WDM E2E路径创建', '网络界面', 'T2000工程', 'SDH E2E路径管理',
           'ETH E2E', 'SDH E2E保护子网', 'RTN业务', '网元搜索', 'MSTP', 'NativeETH', 'OTN', 'RTN', 'SDH E2E',
           'WDM E2E', '传送VRP', '核心配置', '数据', '智能', '传送VRP-MDS', '传送VRP-北向', '传送VRP-告警',
           '传送VRP-性能', '传送VRP-智能'],
    '接入': ['DC', 'APACHE', 'Toolkit', 'ENV', 'xFTP', 'CPESVC', 'XPON', '接入北向接口-框架', '接入LCT', '接入License',
           '接入轮询管理', 'syslog', '调度中心', '定时任务', '接入告警', 'XDSL', 'ATM', '测试台', '接入ETH',
           'ServicePort&PVC', 'VLAN', '组播', '语音业务', 'data collector(非DC)', '升级工具', 'CLI script',
           'NE Lic', '拓扑管理', '物理资源管理', '设备配置', '接入工程/升级', 'SSA', 'SSP',
           'NSE 2700', 'iBridge-SSX', '接入基础API', '接入存量', '接入业务统计', '接入北向接口-业务', 'CMTS',
           'MSO', '智能站点', '接入北向接口'],
    '路由': ['VMF', 'DMF', 'DMS性能', '路由告警', '路由链路', '集群', 'MPLS单站(Tunnel/1711)', 'QoS', 'Bras',
           '即插即用', '安全网元管理', 'IP License', 'IP工程/升级', 'IP 时钟',
           'PTN运维工具', 'VMT框架', 'VRP Adapter框架', '二层单站业务(VPLS/PWE3)', '三层单站业务(L3VPN/路由)',
           'TUNNEL E2E', 'MPLS保护环 E2E', 'L3VPN E2E', '组播业务 E2E', '组合业务 E2E', 'VPLS E2E',
           'IPE2E公共特性', 'TCAT-IP网络调整', 'NativeETH E2E', 'PWE3 E2E', 'TCAT-PWE3业务割接', 'V8网元管理器非业务界面',
           'V5路由器设备管理', 'V8路由器设备管理', 'PTN（V8）设备管理', '测试诊断', '可靠性（OAM/BFD/VRRP）', 'V5路由接口管理',
           'V8路由接口管理', 'PTN（V8）接口管理', 'V5交换机网元管理', 'V8（CE）交换机网元管理', '二层单站非业务（ACL、LLDP、ARP、DHCP）',
           'NMLSDN'],
    '资料': ['资料'],
    '承载': ['PMS-uTraffic对接', 'PMS-实例管理', 'PMS-传送数据采集', 'PMS-IP数据采集', 'PMS-接入数据采集', 'PMS-分布式',
           'PMS-其他', '时钟视图', '报表', '承载业务License',
           '物理存量', '链路管理', '纤缆管理', 'U2100网络特性', 'uTraffic', 'U2100基础特性', '跨域其他特性',
           'uTraffic-报表', 'uTraffic-Gateway', 'uTraffic-采集器', 'uTraffic-自定义报表', 'uTraffic-工程',
           'uTraffic-平台', 'uTraffic-OTN报表', 'uTraffic-存量管理', 'uTraffic-license', 'uTraffic-TWAMP',
           'uTraffic-RTN报表', 'uTraffic-DashBorad', 'uTraffic-物理拓扑', 'uTraffic-IEM',
           'uTraffic-资料', 'uTraffic-4K', 'uTraffic-PTN报表', 'uTraffic-IPRAN报表', 'uTraffic-FTTx报表',
           'uTraffic-大客户专线', 'uTraffic-公共', 'uTraffic-SDN', 'uTraffic-IPFPM',
           '资料-全新安装资料', '资料-补丁安装资料', '资料-流量配置资料',
           '资料-质量配置资料', '资料-SDN资料', '资料-4K资料', '资料-故障和例行维护资料', '资料-探针资料',
           '资料-北向资料', '资料-安全资料',
           '资料-其他研发资料', 'uTraffic-数据库', 'IPRAN-环报表', 'uTraffic-TWAMP其它', 'uTraffic-PSPU',
           'uTraffic-无线设备管理', 'uTraffic-原子路由器管理', 'IPFPM-路径还原', 'IPFPM-其它', 'uTraffic-探针NEU',
           'uTraffic-网元管理', 'uTraffic-拓扑还原', 'uTraffic-地图管理', 'uTraffic-区域地图', 'PTN-环报表', 'PTN-集团报表',
           'uTraffic-Dashboard',
           'uTraffic-基础报表', 'uTraffic-对接', '4K-视频业务体验用户管理', '4K-路径还原', '4K-MDI',
           '4K-全网性能监控管理', '4K-群障', '4K-体验概览', '4K-体验看板', '4K-全网性能监控报表', '4K-双高报表',
           '4K-视频用户体验报表', '4K-个障', '4K-管理考核报表', 'uTaffic-IS', 'Trunk报表', '持续质差报表', 'U2000 框架'],
    '北向': ['CORBA', 'XML', 'SNMP', 'TEXT', 'FTP性能北向', '北向部署工具', '北向License', 'iBridge', 'iBridge-RCA',
           'iBridge-SDN RestAgent', 'iBridge-Text', 'iBridge-OM', 'OMC', '北向-RestConf'],
    '其他': ['主机', '安全加固', '服务器/磁阵'],
    'U2000维护部': ['UEasy'],
    'TMS&ODN': ['iTMS', 'iODN'],
    'NetMatrix': ['CloudVPN', 'CloudEdge', 'SDN WAN', '框架'],
    'N2510': ['AOS-北向TL1', 'AOS-北向SOAP', 'AOS-网络分析', 'AOS-线路测试', 'AOS-线路评估', 'AOS-线路优化', 'AOS-性能预警',
              'AOS-资源管理', 'AOS-ERU工具', 'AOS-站点保障工具', 'LTS-线路测试', 'LTS-资源管理', 'OLS-FTTx报表',
              'OLS-北向TL1', 'OLS-北向SOAP', 'OLS-工程验收', 'OLS-软测', 'OLS-OTDR测试', 'OLS-性能预警',
              'OLS-传送光纤诊断与定位', 'OLS-传送光纤故障监控', 'OLS-设备监控', 'OLS-资源管理', 'OLS-LCT工具',
              'OLS-主动运维', 'OLS-手机App', 'N2510-系统管理', 'N2510-单板软件', 'N2510-单板硬件', 'N2510-网络安全',
              'N2510-License', 'N2510-安装盘', 'N2510-升级包', 'N2510-系统工具', 'N2510-可服务性', 'N2510-配套主机',
              'N2510-配套服务器', 'N2510-操作系统', 'N2510-Oracle数据库', 'N2510-浏览器', 'N2510-产品文档', 'N2510-研发文档'],
    '印研OSS分部': ['uTraffic-告警', '4K-省加地市', 'uTraffic-实时性能&历史性能', 'uTraffic-汇聚计算',
                'uTraffic-北向/PMS反查', 'uTraffic-SPTN/IPRAN2.0'],
    '终端与ODN开发部': ['RMS', '云平台', '智能提速', '分布式工程', '框架/平台', 'APP', '客户端', '北向', 'ACS', 'FS',
                  'ODN', 'TMS平台', '业务'],
    'SDN协同器开发部': ['SDN 框架', 'TSDN', 'SDN WAN', '组合业务', 'SDN 工程', 'CloudVPN'],
    'NCE-T': ['传统波分E2E', '传统波分ASON', '传统波分单站', '传统VRP', 'NCE-核心配置', '平台切换', 'OTN业务发放（portal）', '传送工程', 'L2业务发放（Portal）',
              '生存性分析', '业务重保', '传送存量', '控制南向', '业务框架', '北向接口', 'OTN业务发放（算路）', 'L2业务发放（算路）', '管道',
              '自动化运维服务', '微波SDN', '算法相关','OVPN','生存性分析','故障模拟','大网多域配置Portal'],
    '工具': ['健康检查', '数据采集', '故障定位', '故障定界', '系统卫士','DC升级工具'],
    '基础工程': ['磁阵', '服务器', '工程双机', 'VMware/FusionSphere', '安装部署', '证书管理'],
    '存量': ['统一物理存量管理', '跨域资源采集'],
    'AC-BP': ['AC-BP'],
    'webswing': ['webswing'],
    '框架&跨域': ['Agentintegrate', '传统物理存量', '脚本导入导出', '时钟', '跨域公共', '客户管理', '框架前台', 'uflight', 'NMSMonitorService', '协议栈',
              '框架其他'],
    '公共业务组': ['告警360', '统一portal'],
    'COMMON-资料': ['COMMON-资料'],
    'NCE-Super': ['组合业务', '存量', 'IP+光', '工程', '业务还原', '框架', '业务定义&原子业务', '光原子&采集', 'SPTN&隧道业务'],
    'NCE-分析': ['IPRAN特性', 'PTN特性', '公共-报表框架', '公共-存量同步', '专线运维', '公共-存量适配', 'MPLS网络优化', 'IP网络优化', '公共-工程部署', '公共-采集器',
               'PMS', '集成构建', '大数据计算'],
    'L3层业务管理': ['NCE-IP-隧道策略', 'NCE-IP-路由全局', 'NCE-IP-静态路由', 'NCE-IP-VSI', 'NCE-IP-三层组播', 'NCE-IP-二层组播', 'NCE-IP-策略管理',
                'NCE-IP-IP前缀', 'NCE-IP-VRF', 'NCE-IP-OSPF', 'NCE-IP-ISIS', 'NCE-IP-BGP', 'NCE-IP-PWE3', 'NCE-IP-MPLS',
                'NCE-IP-GRE隧道',
                'NCE-IP-NeService', 'NCE-IP-动态L3VPN',
                'NCE-IP-资源池管理', 'NCE-IP-水平分割组', 'NCE-VRP Adapter框架','NCE-IP工程/升级',
                'NCE-VMT框架', 'NCE-三层单站业务(L3VPN/路由)', 'NCE-二层单站业务(VPLS/PWE3)', 'NCE-MPLS单站(Tunnel/1711)'],
    'L2层业务管理': ['NCE-IP-E2E-MPLS保护环',
                'NCE-IP-E2E-静态TUNNEL', 'NCE-IP-E2E-PWE3', 'NCE-IP-E2E-VPLS', 'NCE-IP-E2E-汇聚业务', 'NCE-IP-E2E-组合业务',
                'NCE-IP-E2E-EVPN业务', 'NCE-IP-E2E-静态L3VPN',
                'NCE-IP-E2E-自动发现IP业务', 'NCE-IP-E2E-Native以太业务', 'NCE-IP-E2E-二层组播业务',
                'NCE-IP-E2E-IP硬管道业务', 'NCE-IP-E2E-TCAT', 'NCE-IP-E2E-SPTN5G', 'NCE-IP-E2E-BGP管理', 'NCE-IP-E2E-免仪表测量',
                'NCE-IP-E2E-业务诊断', 'NCE-IP-E2E-其它'],
    '网元层业务管理': ['NCE-DMF', 'IPLicense', 'IP时钟', 'NCE-V5交换机网元管理', 'V8交换机网元管理', '安全设备管理',
                'NCE-V5路由器设备管理', 'NCE-V8路由器设备管理', 'V5路由器接口', 'V8路由器接口', 'PTNV8设备管理', 'PTNV8接口', 'PTN健康检查', 'ACL', 'LLDP',
                'ARP', 'DHCP', 'OAM', 'BFD', 'VRRP', 'BRAS', '配置回退', '变更审计', '节点冗余（E-APS/E-Trunk)', 'IP性能', '原子路由器',
                '路由器QoS',
                'PTNV8QoS', 'NCE-V8网元管理器非业务界面', 'PTN网元管理器非业务界面', 'FlexEth管理', 'NCE统一资源存量', '网元时间同步', '光功率管理',
                '光功率管理'],
    '网络OAM管理': ['NCE-路由告警', 'NCE-即插即用', 'NCE-测试诊断','NCE-NMLSDN', '集成脚本工具(ipisstar)', 'CU分离', 'SDN2.0（VLL业务）'],
    '网络路径管理': ['VTEM（业务管理）', 'GPATH（拓扑管理/算路管理）', 'PCEP（业务交互通道）', '算法（业务算路）'],
    'IP调优管理': ['ITEM（网络调优/网元调优）',
               'BGP（动态路由协议/拓扑收集）', 'SNCcfg（AC配置）', 'WebUI（页面）'],
    '隧道服务管理': ['NCE-IP动态RSVP-TE业务', 'NCE-IP动态SR-TE业务', 'NCE-IP动态SR-TP业务', 'AC侧nettetunnel', 'PCEadapter（控制域proto消息通信）'],
    '业务集成管理': ['L3拓扑', '三方设备管理', '路由策略'],
    'Campus控制器产品部': [],
    'DCN控制器产品部': [],
    'Super控制器产品部': ['领域业务', '增值业务', '基础架构', '公共业务', '传输基础业务', '还原业务', '跨层业务', 'IP基础业务',
                    '核心业务', '跨域业务'],
    'TSDN控制器产品部': [],
    'WAN控制器产品部': []
}

# 开发LM和对应的特性
LMList = {
    "chenyuan_00258251": ["客户端", "北向", "ACS", "FS", "ODN", "TMS平台", "业务","iODN", "iTMS"],
    "chenlening_00294178": ["uTraffic-SDN"],
    "wanchengpeng_00164117": ["TSDN", "公共-存量适配", "MPLS网络优化", "IP网络优化", "公共-工程部署"],
    "liulingxian_00266809": ["WDM E2E保护子网", "OTN-其他", "智能-其他", "WDM E2E路径搜索", "传送VRP-告警", "传送VRP-性能", "WDM E2E-其他",
                             "网络界面", "OTN配置", "OTN业务", "传送VRP-通用配置", "WDM E2E路径管理", "传送VRP-分组特性",
                             "波分", "WDM E2E路径创建", "波分智能", "传送VRP-网元通讯", "传送VRP-框架", "传送VRP-其他",
                             "波分WebLCT", "传送VRP-波分特性", "传送VRP -SDH特性", "海缆", "OTN", "WDM E2E", "传送VRP", "传送VRP-MDS",
                             "传送VRP-北向", "传送VRP-告警", "传送VRP-性能", "传送VRP-智能", "传送 OTN TCAT", "传统波分E2E", "传统波分ASON",
                             "传统波分单站", "传统VRP"],
    "wanliang_00343524": ["SDH E2E路径搜索", "ETH E2E路径创建", "WebLCT公共", "MSTP配置", "SDH E2E-其他", "数据业务", "MSTP业务",
                          "ETH E2E路径搜索", "数据WebLCT", "数据 -其他", "SDH E2E路径创建", "传送TCAT", "RTN业务", "微波WebLCT", "RTN-其他",
                          "数据配置", "SDH E2E路径管理", "ETH E2E路径管理", "ETH E2E-其他", "RTN配置", "SDH E2E保护子网", "MSTP-其他",
                          "ETH E2E", "SDH智能", "MSTP", "NativeETH", "RTN", "SDH E2E", "数据", "智能",
                          "L2业务发放（Portal）", "生存性分析", "业务重保", "传送存量",'OVPN','生存性分析','故障模拟','大网多域配置Portal'],
    "laipeijun_00391486": ["iBridge-RCA", "iBridge-SDN RestAgent", "OMC", "iBridge-Text", "iBridge-OM", "XML",
                           "iBridge", "CORBA", "TEXT", "SNMP", "北向License", "北向部署工具", "FTP性能北向", "北向-RestConf"],
    "other": ["主机"],
    "caopengfei_00330715": ["ENV", "Toolkit", "NE Lic", "xFTP", "APACHE", "DC","DC升级工具"],
    "wangzhuo_00399518": ["UEasy", "健康检查", "数据采集", "故障定位", "故障定界", "系统卫士"],
    "guzhenyu_00200214": ["工程平台UniEP", "CloudSOP(UniEP)"],
    "maluo_00290915": ["PaaS"],
    "qinyi_00398210": ["SDN工程", "SDN 框架", "基础架构"],
    "zhangshouxin_00375597": ["MSO", "AOS-北向TL1", "AOS-北向SOAP", "AOS-网络分析", "AOS-线路测试", "AOS-线路评估", "AOS-线路优化",
                              "AOS-性能预警",
                              "AOS-资源管理", "AOS-ERU工具", "AOS-站点保障工具", "LTS-线路测试", "LTS-资源管理", "OLS-FTTx报表",
                              "OLS-北向TL1", "OLS-北向SOAP", "OLS-工程验收", "OLS-软测", "OLS-OTDR测试", "OLS-性能预警",
                              "OLS-传送光纤诊断与定位", "OLS-传送光纤故障监控", "OLS-设备监控", "OLS-资源管理", "OLS-LCT工具",
                              "OLS-主动运维", "OLS-手机App", "N2510-系统管理", "N2510-单板软件", "N2510-单板硬件", "N2510-网络安全",
                              "N2510-License", "N2510-安装盘", "N2510-升级包", "N2510-系统工具", "N2510-可服务性", "N2510-配套主机",
                              "N2510-配套服务器", "N2510-操作系统", "N2510-Oracle数据库", "N2510-浏览器", "N2510-产品文档", "N2510-研发文档","iBridge-SSX",
                              "ServicePort&PVC", "CPESVC", "SSP", "接入LCT", "测试台", "语音业务", "CMTS", "接入ETH","物理资源管理", "接入北向接口-框架",
							  "syslog", "定时任务", "接入轮询管理","接入工程/升级", "接入存量", "拓扑管理", "升级工具", "接入告警", "调度中心",
                              "设备配置", "接入基础API", "接入北向接口", "ATM", "接入业务统计", "XPON", "组播",
                              "VLAN", "CLI script", "接入北向接口-业务", "XDSL", "智能站点"],
    "yinzhiqiang_00216300": ["iWeb平台"],
    "zhoujihong_00334392": ["IPRAN-环报表", "uTraffic-原子路由器管理", "uTraffic-TWAMP", "IPFPM-路径还原", "uTraffic-无线设备管理",
                            "uTraffic-IPRAN报表",
                            "uTraffic-PSPU", "uTraffic-大客户专线", "uTraffic-探针NEU", "IPFPM-其它", "uTraffic-TWAMP其它",
                            "uTraffic-FTTx报表", "uTraffic-IPFPM",
                            "uTraffic-网元管理", "uTraffic-拓扑还原"],
    "zhouzheng_00247283": ["资料"],
    "zhanhuajie_00329574": ["4K-全网性能监控报表", "4K-视频用户体验报表", "4K-全网性能监控管理", "uTraffic-4K", "持续质差报表", "4K-管理考核报表", "4K-个障",
                            "Trunk报表", "4K-体验概览", "4K-体验看板", "4K-视频业务体验用户管理", "4K-双高报表", "4K-路径还原", "4K-MDI", "4K-群障"],
    "linzhifeng_00275309": ["集成构建"],
    "chenlening_00294178": ["uTraffic-数据库", "uTraffic-工程", "uTraffic-存量管理"],
    "wanghongxin_00330334": ["T2000工程", "PTN配置", "界面公共", "PTN界面", "核心配置-其它", "网元安全管理", "MML远维", "PTN业务", "性能框架",
                             "传送License", "告警框架",
                             "mirror db", "网元搜索", "持久层框架", "基本配置", "网元通信", "传送工程/升级", "进程框架", "Adapter框架", "网元迁移",
                             "分布式框架",
                             "脚本导入导出框架", "核心配置", "平台切换", "OTN业务发放（portal）", "传送工程","NCE-核心配置"],
    "shiyongguang_00317193": ["VRP Adapter框架","NCE-VRP Adapter框架", "VMF", "IP工程/升级","NCE-IP工程/升级", "VMT框架", "NCE-VMT框架", "二层单站业务(VPLS/PWE3)","NCE-二层单站业务(VPLS/PWE3)",
                              "MPLS单站(Tunnel/1711)", "NCE-MPLS单站(Tunnel/1711)","NCE-IP-隧道策略", "NCE-IP-路由全局", "NCE-IP-静态路由", "NCE-IP-VSI",
                              "NCE-IP-二层组播", "NCE-IP-策略管理", "NCE-IP-IP前缀",
                              "NCE-IP-VRF", "NCE-IP-OSPF", "NCE-IP-ISIS", "NCE-IP-BGP", "NCE-IP-PWE3", "NCE-IP-MPLS",
                              "NCE-IP-GRE隧道", "NCE-IP-NeService", "NCE-IP-资源池管理"],
    "chengweiqiang_00317614": ["data collector(非DC)", "NSE 2700"],
    "shuaiyan_00121192": ["CloudEdge"],
    "yangzhenhua_00246394": ["Bras", "集群", "PTN运维工具", "QoS", "DMF",  "NCE-DMF", "路由链路", "DMS性能", "IP时钟", "安全网元管理",
                             "V8网元管理器非业务界面", "NCE-V8网元管理器非业务界面","IPLicense", "V5路由器设备管理","NCE-V5路由器设备管理",
                             "V8路由器设备管理", "NCE-V8路由器设备管理","V5路由器接口","V8路由器接口","PTN（V8）设备管理","PTNV8设备管理","PTNV8接口",
                             "可靠性（OAM/BFD/VRRP）", "V5路由接口管理", "V8路由接口管理", "PTN（V8）接口管理","PTN健康检查","ACL","LLDP","ARP","DHCP","OAM","BFD",
                             "V5交换机网元管理","NCE-V5交换机网元管理", "V8交换机网元管理","安全设备管理","VRRP","BRAS","配置回退","变更审计","节点冗余（E-APS/E-Trunk)",
                             "V8（CE）交换机网元管理", "二层单站非业务（ACL、LLDP、ARP、DHCP）","IP性能","原子路由器","路由器QoS","PTNV8QoS","PTN网元管理器非业务界面",
                             "FlexEth管理","NCE统一资源存量","网元时间同步","光功率管理"],
    "zhanghui_00180241": ["L3VPN E2E", "TCAT-IP网络调整", "组播业务 E2E", "TUNNEL E2E", "MPLS保护环 E2E", "PWE3 E2E",
                          "TCAT-PWE3业务割接", "IPE2E公共特性", "VPLS E2E",
                          "NativeETH E2E", "组合业务 E2E", "NCE-IP-E2E-MPLS保护环", "NCE-IP-E2E-静态TUNNEL", "NCE-IP-E2E-PWE3",
                          "NCE-IP-E2E-VPLS", "NCE-IP-E2E-汇聚业务", "NCE-IP-E2E-组合业务", "NCE-IP-E2E-EVPN业务",
                          "NCE-IP-E2E-静态L3VPN", "NCE-IP-E2E-自动发现IP业务", "NCE-IP-E2E-Native以太业务", "NCE-IP-E2E-二层组播业务",
                          "NCE-IP-E2E-IP硬管道业务",
                          "NCE-IP-E2E-TCAT", "NCE-IP-E2E-SPTN5G", "NCE-IP-E2E-BGP管理", "NCE-IP-E2E-免仪表测量",
                          "NCE-IP-E2E-业务诊断", "NCE-IP-E2E-其它"],
    "liangyikang_00468709": ["imap平台", "iMap平台License", "TOMCAT"],
    "hanzhaoguo_00218793": ["CloudSOP(业务)"],
    "wangyunpeng_00372853": ["uTraffic-公共", "uTraffic-SPTN/IPRAN2.0", "uTraffic-实时性能&历史性能", "uTraffic-告警",
                             "uTraffic-北向/PMS反查", "uTraffic-采集器",
                             "uTraffic-汇聚计算", "4K-省加地市"],
    "zhangyunliang_00223922": ["uTraffic-平台cloudsop", "uTraffic-平台OSS3.0", "uTraffic-平台"],
    "caiyongzhan_00303386": ["资料-安全资料", "资料-流量配置资料", "资料-SDN资料", "资料-其他研发资料", "资料-北向资料", "uTraffic-资料", "资料-故障和例行维护资料",
                             "资料-补丁安装资料", "资料-质量配置资料", "资料-探针资料", "资料-全新安装资料", "资料-4K资料"],
    "chenli_00178570": ["uTraffic-OTN报表", "uTraffic-PTN报表", "uTraffic-license", "uTraffic-RTN报表", "报表",
                        "uTraffic-DashBorad", "uTraffic", "uTraffic-报表",
                        "uTraffic-IEM", "uTraffic-Gateway", "uTraffic-区域地图", "uTraffic-自定义报表", "PTN-环报表", "PTN-集团报表",
                        "uTraffic-物理拓扑", "uTaffic-IS",
                        "uTraffic-对接", "uTraffic-基础报表", "uTraffic-Dashboard", "uTraffic-地图管理", "PTN特性", "公共-报表框架",
                        "公共-存量同步", "专线运维"],
    "lepei_00173412": ["组合业务"],
    "shuaiyan_00365292": ["CloudVPN", "核心业务"],
    "zhaoguodong_00425795": [],
    "zhuxuhui_00130480": ["SSA"],
    "zhangyang_00334788": ["SDN WAN", "业务定义&原子业务", "公共业务"],
    "yongjianguo_00326378": ["SDN WAN"],
    "chenlinkun_00287251": ["路由告警", "NCE-路由告警","诊断&OAM", "即插即用","NCE-即插即用", "光功率管理", "测试诊断","NCE-测试诊断", "NMLSDN", "NCE-NMLSDN", "集成脚本工具(ipisstar)", "CU分离",
                            "SDN2.0（VLL业务）"],
    "chenli_00306421": ["框架", "Veritas"],
    "jiaoshi_00343677": ["DB", "OS", "磁阵", "服务器","服务器/磁阵"],
    "shixiang_00187237": ["RMS", "智能提速", "框架/平台", "APP", "分布式工程", "云平台"],
    "yuzhenming_00342919": ["PMS-传送数据采集", "链路管理", "工程双机", "PMS-uTraffic对接", "PMS-IP数据采集", "承载业务License", "安全加固", "时钟视图",
                            "PMS-实例管理",
                            "U2100基础特性", "PMS-分布式", "升级/补丁框架", "PMS-接入数据采集", "工程维护工具", "物理存量", "PMS-其他",
                            "工程安装框架",
                            "纤缆管理", "跨域其他特性", "U2100网络特性", "公共-采集器", "PMS"],
    "sunlinlin_00449821": ["领域业务"],
    "meixiaoling_00411974": ["VTEM（业务管理）", "GPATH（拓扑管理/算路管理）", "PCEP（业务交互通道）", "算法（业务算路）"],
    'jiaxianbo_00281886': ["ITEM（网络调优/网元调优）", "BGP（动态路由协议/拓扑收集）", "SNCcfg（AC配置）", "WebUI（页面）"],
    "zhangcong_00367555": ["NCE-IP动态RSVP-TE业务", "NCE-IP动态SR-TE业务", "NCE-IP动态SR-TP业务", "AC侧nettetunnel",
                           "PCEadapter（控制域proto消息通信）"],
    "yanhao_00180558": ["L3拓扑", "三方设备管理", "路由策略","NCE-IP-水平分割组"],
    "zhanchang_00368856": ["控制南向", "业务框架", "北向接口"],
    "yaofeng_00201271": ["OTN业务发放（算路）", "L2业务发放（算路）", "管道"],
    "xiangwei_00442543": ["自动化运维服务", "微波SDN", "算法相关"],
    "maokai_00325469": ["工程双机", "VMware/FusionSphere", "安装部署", "证书管理", "统一物理存量管理", "跨域资源采集", "告警360",
                        "统一portal", "U2000 框架"],
    "zhangguiping_00376372": ["AC-BP"],
    "huangzengjun_00287220": ["webswing", "Agentintegrate", "传统物理存量", "脚本导入导出", "时钟", "跨域公共", "客户管理", "框架前台", "uflight",
                              "NMSMonitorService",
                              "协议栈", "框架其他"],
    "zhengxuewei_00177746": ["COMMON-资料"],
    "luolei_00245547": ["IPRAN特性"],
    "zhanglingzhi_00342954": ["大数据计算"],
    "jiangxingfeng_00362412": ["增值业务"],
    "zhengting_00219142": ["传输基础业务", "光原子&采集", "SPTN&隧道业务"],
    "wanchengpeng_00443901": ["业务还原"],
    "wanglan_00227452": ["跨层业务", "IP+光", "工程"],
    "pengqiushi_00289217": ["IP基础业务"],
    "yemin_00376721": ["跨域业务", "组合业务", "存量"],
    "zhaowei_00303021":["NCE-IP-动态L3VPN","三层单站业务(L3VPN/路由)","NCE-三层单站业务(L3VPN/路由)","NCE-IP-三层组播"]
}

# 开发LM对应开发部
LMToDept = {
    'jiaoshi_00343677': '传送',
    'zhangyunliang_00223922': '平台',
    'maluo_00290915': '平台',
    'maokai_00325469': '承载',
    'wangyunpeng_00372853': '承载',
    'chenhaibo_00334316': '承载',
    'fengjianli_00335896': '承载',
    'zhoujihong_00334392': '承载',
    'chenlening_00294178': '承载',
    'wanliang_00118433': '传送',
    'linhanzhong_64481': '传送',
    'chenli_00306421': '传送',
    'chenli_00178570': '承载',
    'liulingxian_00266809': '传送',
    'wanliang_00343524': '传送',
    'zhaoguodong_00425795': '接入',
    'zhangshouxin_00132963': '接入',
    'malimin_00258246': '终端与ODN开发部',
    'chenyuan_00258251': '终端与ODN开发部',
    'zhuxuhui_00130480': '接入',
    'chenlinkun_00287251': '路由',
    'wanghaiwei_52487': '路由',
    'luogaofeng_00222783': '路由',
    'zhanglaiqiang_00215725': '路由',
    'shiyongguang_00317193': '路由',
    'yinzhiqiang_00216300': '平台',
    'zhanhuajie_00329574': '承载',
    'chenlening_00294178': '承载',
    'lixiang_00256213': '北向',
    'chenhong_00210296': '承载',
    'shilifeng_00210302': '承载',
    'other': '主机',
    'panyi_00330136': '承载',
    'liangyikang 00468709': '平台',
    'chenqi_00257017': '承载',
    'shaozhenghua_00064102': '路由',
    'caopengfei_00330715': '接入',
    'chengweiqiang_00317614': 'DC/NSE',
    'wanhao_00113463': '路由',
    'jiaxianbo_00281886': '路由',
    'wangzhuo_00399518': '维护',
    'zhouzheng_00247283': '资料',
    'yangchunxiang_00338779': '路由',
    'zhanghui_00180241': '路由',
    'zhangjianzheng_00258276': '传送',
    'guzhenyu_00200214': '平台',
    'zhaowei_00303021': '路由',
    'wanghongxin_00330334': '传送',
    'yanzhenshan_00129025': '传送',
    'zhaochao_00222782': '承载',
    'shenheng_00266400': '传送',
    'yongjianguo_00326378': '路由',
    'wanchengpeng_00164117': '传送',
    'caiyongzhan_00303386': '承载',
    'hujunqin_00343607': '承载',
    'kulbhushanr_70495': '承载',
    'songshirong_00332908': '承载',
    'xuhaibin_00267227': '承载',
    'laipeijun_00391486': '北向',
    'zhangshouxin_00375597': '接入',
    'yuzhenming_00342919': '承载',
    'yangzhenhua_00246394': '路由',
    'shixiang_00187237': '终端与ODN开发部',
    'wanchengpeng 00443901': 'SDN协同器开发部',
    'lepei_00173412': 'SDN协同器开发部',
    "sunlinlin_00449821": 'Super控制器产品部',
    "jiangxingfeng_00362412": 'Super控制器产品部',
    "qinyi_00398210": 'Super控制器产品部',
    "zhangyang_00334788": 'Super控制器产品部',
    "zhengting_00219142": 'Super控制器产品部',
    'linzhifeng_00275309': '承载',
    'hanzhaoguo_00218793': '平台',
    'meixiaoling_00411974': '路由',
    'zhangcong_00367555': '路由',
    'yanhao_00180558': '路由',
    'zhanchang_00368856': '传送',
    'yaofeng_00201271': '传送',
    'xiangwei_00442543': '传送',
    'zhangguiping_00376372': '承载',
    'huangzengjun_00287220': '承载',
    'zhengxuewei_00177746': '承载',
    'luolei_00245547': '承载',
    'zhanglingzhi_00342954': '承载',
    'wanglan 00227452': '承载',
    "wanchengpeng_00443901": 'Super控制器产品部',
    "wanglan_00227452": 'Super控制器产品部',
    "pengqiushi_00289217": 'Super控制器产品部',
    "shuaiyan_00365292": 'Super控制器产品部',
    "yemin_00376721": 'Super控制器产品部'
}

# 维护LM和对应的特性
MatainceLMList = {
    'wanliang_00118433': ['MSTP', 'RTN', 'OTN', '波分'],
    'lianfengwei_00330187': ['CPESVC', 'XPON', '接入北向接口', '接入LCT', '接入License', '接入轮询管理',
                             'syslog', '调度中心', '定时任务', '接入告警', 'XDSL', 'ATM', '测试台',
                             '拓扑管理', '物理资源管理', '设备配置', '接入ETH', 'ServicePort&PVC',
                             'VLAN', '组播', '语音业务'],
    'tianxin_00245566': ['VMF', 'DMF', '报表', 'DMS性能', '路由告警', '路由链路', '集群', '单站业务管理', 'QoS', 'Bras',
                         '即插即用', '安全网元管理'],
    'wangzhuo_00151255': ['UEasy'],
    'wenwuqiang_00365331': ['SDH E2E路径创建', '告警框架', 'PTN界面', '数据业务', '传送VRP-其他', 'OTN-其他',
                            'SDH E2E路径搜索', 'RTN配置', 'PTN配置', 'WDM E2E路径管理', '智能-其他', 'MSTP业务',
                            '数据配置', 'SDH智能', 'ETH E2E路径创建', '传送VRP-分组特性', '界面公共', '网元通信',
                            '传送VRP-框架', 'RTN-其他', '传送VRP-告警', 'ETH E2E路径搜索', 'WDM E2E路径搜索',
                            '网元安全管理', 'MML远维', '海缆', '波分', 'ETH E2E路径管理', '分布式框架', '传送TCAT',
                            'ETH E2E-其他', '持久层框架', '传送VRP-通用配置', '波分智能', '数据WebLCT', '核心配置-其它',
                            '性能框架', '网元迁移', 'WebLCT公共', 'WDM E2E-其他', 'OTN配置', '进程框架',
                            '传送VRP-性能', '微波WebLCT', '传送VRP-网元通讯', '基本配置', 'SDH E2E-其他', '传送工程/升级', 'WDM E2E保护子网',
                            '波分WebLCT', 'mirror db',
                            'MSTP-其他', 'Adapter框架', ' 数据 -其他', '传送VRP -SDH特性', '脚本导入导出框架',
                            'MSTP配置', '传送License', 'PTN业务', '传送VRP-波分特性', 'OTN业务', 'WDM E2E路径创建', '网络界面', 'T2000工程',
                            'SDH E2E路径管理',
                            'ETH E2E', 'SDH E2E保护子网', 'RTN业务', '网元搜索'],
    'liurenjie 00177360': ['北向-RestConf']
}

# Top局点信息
TopList = [
    {'局点': '英国MBNL', '产品': 'U2000-IP(PTN);U2000-IP(Route)', '片区': '欧洲', '责任主管': 'pengshaobo_00152343;lichangli_56635',
     '责任SE': 'niezhibin_61334'},
    {'局点': '英国BT', '产品': 'U2000-IP(PTN);U2000-IP(Route)', '片区': '欧洲', '责任主管': 'yangyanze_64202',
     '责任SE': 'zhangjisheng_62760'},
    {'局点': '上海联通', '产品': 'U2000-IP(PTN);U2000-IP(Route)', '片区': '中国', '责任主管': 'shaoshixin_00301751',
     '责任SE': 'huyahong_00162907'},
    {'局点': '日本KDDI', '产品': 'U2000-IP(PTN)', '片区': '东亚', '责任主管': 'peifeiyue_43185', '责任SE': 'liubo_00046261'},
    {'局点': '土耳其VDF', '产品': 'U2000-IP(PTN)', '片区': '中亚', '责任主管': 'shilifeng_35883', '责任SE': 'zhaoyao_41516'},
    {'局点': '西班牙VDF', '产品': 'U2000-IP(PTN);U2000-T', '片区': '欧洲', '责任主管': 'lvxinping_00120187',
     '责任SE': 'laiguiyong_00101257;chenxian_36335'},
    {'局点': '福州联通', '产品': 'U2000-T', '片区': '中国', '责任主管': 'yangyong_62244', '责任SE': 'zengjianguo_00152332'},
    {'局点': '土耳其SOL', '产品': 'U2000-T', '片区': '中亚', '责任主管': 'machongxi_37991', '责任SE': 'wangwei_37859'},
    {'局点': '俄罗斯Megafon', '产品': 'U2000-T', '片区': '中亚', '责任主管': 'wangfen_61594', '责任SE': 'laiguiyong_00101257'},
    {'局点': '瑞士电信', '产品': 'U2000-T', '片区': '欧洲', '责任主管': 'chenhong_35752', '责任SE': 'xiaochaojun_00162712'},
    {'局点': '印度VDF', '产品': 'U2000-T', '片区': '印度', '责任主管': 'zhulei_00210433', '责任SE': 'fangchao_00162708'},
    {'局点': '浙江移动', '产品': 'U2000-B', '片区': '中国', '责任主管': 'zengxiaolong_00147142', '责任SE': 'bigang_00109168'},
    {'局点': '法国FT', '产品': 'U2000-B', '片区': '欧洲', '责任主管': 'yangling_39940', '责任SE': ''},
    {'局点': '马来西亚TM', '产品': 'U2000-B', '片区': '亚太', '责任主管': 'zhongwenyu_00109166', '责任SE': 'xiegengsheng_00035916'},
    {'局点': '上海电信', '产品': 'U2000-B', '片区': '中国', '责任主管': 'dingyueming_00152344', '责任SE': 'lvtao_41385'},
    {'局点': '英国BT', '产品': 'U2000-B', '片区': '欧洲', '责任主管': 'zengxiaolong_00147142', '责任SE': 'huangping_00152324'},
    {'局点': '北京联通', '产品': 'U2000-B', '片区': '中国', '责任主管': 'chenmin_00101318', '责任SE': 'wujianbo_64329'},
    {'局点': '土耳其TT', '产品': 'U2000-B', '片区': '中亚', '责任主管': 'linwenting_00134124', '责任SE': 'yangkan_40389'},
    {'局点': '沙特STC', '产品': 'ALL', '片区': '中东北非', '责任主管': 'lijianhui_00162723', '责任SE': 'dongjie_37985'},
    {'局点': '卡塔尔Qtel', '产品': 'ALL', '片区': '中东北非', '责任主管': 'zhongjunshuai_64268', '责任SE': ''}
]

# 超期问题发送至LM邮件抄送人
reportLM_CC = '''z00210433@notesmail.huawei.com,
               c00101318@notesmail.huawei.com, p47183@notesmail.huawei.com, d00231672@notesmail.huawei.com, 
               l00112051@notesmail.huawei.com,l68925@notesmail.huawei.com,
               x00100648@notesmail.huawei.com, m00110871@notesmail.huawei.com, l00142547@notesmail.huawei.com'''

# Top局点信息的发送人和抄送人
Top_CC = '''c00101318@notesmail.huawei.com,l00222901@notesmail.huawei.com,p47183@notesmail.huawei.com,
          z00210433@notesmail.huawei.com,g00258409@notesmail.huawei.com,t52324@notesmail.huawei.com,
          y45668@notesmail.huawei.com,z48374@notesmail.huawei.com,
          d00231672@notesmail.huawei.com,c00160602@notesmail.huawei.com,
          l00112051@notesmail.huawei.com, l68925@notesmail.huawei.com'''

# 管理级别信息的主送人和抄送人
ManageSender = '''c00101318@notesmail.huawei.com,l00222901@notesmail.huawei.com,p47183@notesmail.huawei.com,
          z00210433@notesmail.huawei.com,g00258409@notesmail.huawei.com,t52324@notesmail.huawei.com,
          y45668@notesmail.huawei.com,z48374@notesmail.huawei.com,
          d00231672@notesmail.huawei.com,c00160602@notesmail.huawei.com,
          l00112051@notesmail.huawei.com, l68925@notesmail.huawei.com'''

# iCare单超期问题的抄送人
ExtendDate_CC = 'x00114663@notesmail.huawei.com, l00112051@notesmail.huawei.com, z48374@notesmail.huawei.com, l00178066@notesmail.huawei.com, h00191256@notesmail.huawei.com, l00192919@notesmail.huawei.com, y00201396@notesmail.huawei.com'

# U2000-T TDT对应项目组信息
moduleDict = {'传送单站': ['DataCollector', 'MSTP', 'RTN', '波分', '海缆', '核心配置', '配置界面', '数据单站', '通用技术', '维护', '智能'],
              '工程': ['工程', '工程平台'],
              '北向': ['北向'],
              '端到端': ['网络后台', '数据网络后台', '网络界面', 'TCAT', '传送E2E'],
              'PTN': ['PTN业务', 'PTN配置', 'PTN界面'],
              '资料': ['资料'],
              '跨域': ['跨域'],
              'IMAP平台': ['中软iMAP平台'],
              'CMF': ['DC/Toolkit']
              }
# 面问题开发部
mDeptList = ['传送开发部', '接入开发部', 'IP开发部', '承载开发部', '设计部', '北向开发部', '平台开发部', '维护部', '架构TMG', '编程TMG', '数据库TMG', '界面TMG',
             '安全TMG', '升级TMG', '责任未定']

# 基线版本与TDT对应关系
pdt2MatchList = {"U2000-T": ["IMANAGERMDS6630", "IMANAGERNBI", "T2000", "TRANSDATA", "U2000-T", "U2000LCT"],
                 "U2000-B": ["BT NGA 4.1.08", "IMANAGERN2000BMS", "U2000-B", "U2000DC", "IMANAGERCMF(DC)"],
                 "U2000-IP(PTN)": [],
                 "U2000-IP(Router)": ["DMSV500R003", "IMANAGERN2000DMS", "IMANAGERU2000-IP", "IMANAGERVMF", "U2000-R",
                                      "U2000-VSM", "IMANAGERCMF", "IMANAGERPMS", "IWEB-REPORTV100R007C07B037SPC090",
                                      "U2000-IP"],
                 "U2000-I": ["IMANAGERE2E", "T2100", "U2000-I", "U2100"],
                 "uTraffic": ["UTRAFFIC"]
                 }

pdt2NoMatch = {"U2000-IP(Router)": ["IMANAGERCMF(DC)"],
               "U2000-I": ["U2000-IP", "IMANAGERU2000-IP"]
               }

# 特性对应关注人
feature2Person = {
    'DC': 'z00192701',
    'Toolkit': 'z00192701',
    'xFTP': 'z00192701',
    'ENV': 'z00192701',
    'NE Lic': 'z00192701'
}

#######################控制域合并到维护平台时新增###########################

# 问题来源
issueSource = ['网上问题', '大局支撑', '普通局点问题', '巡检问题', '升级割接保障', '对外测试']

# 控制域产品对应设备类型
controlPDT2DeviceType = {
    'AC-Campus': ['AC-Campus', 'AC-CloudManager', 'CloudCampus', 'CloudVPN', 'EC-IOT', 'Policy Center', 'SD-WAN',
                  'TSM'],
    'AC-DCN': ['AC-DCN'],
    'AC-WAN': ['AC-WAN'],
    'T-SDN': ['T-SDN']
}
