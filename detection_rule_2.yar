rule Windows_GrimResource_MMC {
    meta:
        author = "ZERODETECTION"
        reference = "https://www.elastic.co/security-labs/GrimResource"
        reference_sample = ""
        arch_context = "x86"
        scan_context = "file, memory"
        license = "MIT"
        os = "windows"
    strings:
        $xml = "<?xml"
        $a = "MMC_ConsoleFile"
        $b = /apds\.dll|res:\/\/|javascript:eval\(|\.loadXML\(/  // Combined regex for obfuscation patterns
    condition:
        $xml at 0 and $a and $b
}
