from ...core.config_manager import Config

i = Config.CMD_SUFFIX

class BotCommands:
    StartCommand = f"start{i}"
    MirrorCommand = [f"mirror1{i}", f"mz1{i}"]
    QbMirrorCommand = [f"qbmirror1{i}", f"qm1{i}"]
    JdMirrorCommand = [f"jdmirror1{i}", f"jm1{i}"]
    YtdlCommand = [f"ytdl1{i}", f"y1{i}"]
    NzbMirrorCommand = [f"nzbmirror1{i}", f"nm1{i}"]
    LeechCommand = [f"leech1{i}", f"l1{i}"]
    QbLeechCommand = [f"qbleech1{i}", f"ql1{i}"]
    JdLeechCommand = [f"jdleech1{i}", f"jl1{i}"]
    YtdlLeechCommand = [f"ytdlleech1{i}", f"yl1{i}"]
    NzbLeechCommand = [f"nzbleech1{i}", f"nl1{i}"]
    CloneCommand = f"clone1{i}"
    CountCommand = f"count{i}"
    DeleteCommand = f"del{i}"
    CancelTaskCommand = [f"cancel{i}", f"c{i}"]
    CancelAllCommand = f"cancelall{i}"
    ForceStartCommand = [f"forcestart{i}", f"fs{i}"]
    ListCommand = f"list{i}"
    SearchCommand = f"search1{i}"
    StatusCommand = f"status1{i}"
    UsersCommand = f"users{i}"
    AuthorizeCommand = f"auth{i}"
    UnAuthorizeCommand = f"unauth{i}"
    AddSudoCommand = f"addsudo{i}"
    RmSudoCommand = f"rmsudo{i}"
    PingCommand = f"ping1{i}"
    RestartCommand = f"restart1{i}"
    StatsCommand = f"stats1{i}"
    HelpCommand = f"help{i}"
    LogCommand = f"log{i}"
    ShellCommand = f"shell{i}"
    AExecCommand = f"aexec{i}"
    ExecCommand = f"exec{i}"
    ClearLocalsCommand = f"clearlocals{i}"
    BotSetCommand = [f"bsetting1{i}", f"bs1{i}"]
    UserSetCommand = [f"usetting1{i}", f"us1{i}"]
    SelectCommand = f"sel{i}"
    RssCommand = f"rss{i}"
    NzbSearchCommand = f"nzbsearch{i}"
