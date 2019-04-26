#!/usr/bin/python3
import atexit
import subprocess
import shlex
import time

pprx_args =         shlex.split('pprx -f opt_files/aritgo_pprx.opt')
tee_args =          'tee ppengine_in output_files/pprx.gbx < pprx_out > /dev/null'
ppengine_args =     shlex.split('ppengine -f opt_files/aritgo_ppengine.opt')
netserve_args =     shlex.split('socat -U TCP-LISTEN:50000,fork,reuseaddr SYSTEM:"tail -c +1 -f output_files/precise.gbx"')

def cleanup():
        print('KILLING PPRX')
        pprx.kill()
        print('KILLING TEE')
        tee.kill()
        print('KILLING PPENGINE')
        ppengine.kill()
        print('KILLING NETSERVE')
        netserve.kill()
atexit.register(cleanup)

while True:
    # Open pprx and ppengine (must be done together each time due to the semantix of unix named pipes)
    pprx = subprocess.Popen(pprx_args)
    tee = subprocess.Popen(tee_args, shell=True)
    ppengine = subprocess.Popen(ppengine_args)
    netserve = subprocess.Popen(netserve_args)


    # Busy loop making sure all of our subprocesses are still alive
    while True:
        ppengine.poll()
        if ppengine.returncode is not None:
            print('ppengine has died. Restarting Stack...')
            break

        tee.poll()
        if tee.returncode is not None:
            print ('tee has died. Restarting Stack...')
            break

        pprx.poll() 
        if pprx.returncode is not None:
            print ('pprx has died. Restarting stack...')
            break


        netserve.poll()
        if netserve.returncode is not None:
            print('TCP socket server has died. Restarting Stack......')
            break
        time.sleep(1)

    cleanup()

    time.sleep(2)

print('Stack running...')
