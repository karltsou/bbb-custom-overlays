### Screen on

```
$ xset -display :0.0 dpms force on
```

### Screen off

```
$ xset -display :0.0 s noblank
$ xset -display :0.0 s activate
```

### CPU change freq between 300 to 1000 MHz

```
$ sudo cpufreq-set -f 300Mhz
$ sudo cpufreq-set -f 1000Mhz
```

### CPU current and support freq

```
$ cpufreq-info
```

