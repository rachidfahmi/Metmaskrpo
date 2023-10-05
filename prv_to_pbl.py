from coincurve import PrivateKey
from bip44 import Wallet
from bip44.utils import get_eth_addr
from generate import genrat


def prvtpub():


    mnemonic = genrat()
    print(mnemonic)
    w = Wallet(mnemonic)
    sk, pk = w.derive_account("eth", account=0)
    sk = PrivateKey(sk)
    sk.public_key.format() == pk
    True
    return get_eth_addr(pk)
   
