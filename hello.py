import idc
import idascript

print("Hello world from IDAPython")
for i in range(1, len(idc.ARGV)):
    print("ARGV[%d]=%s" % (i, idc.ARGV[i]))

idc.Exit(0)