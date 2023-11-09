"use client"
import Link from "next/link"
import Image from "next/image"
import Furina from '@/public/furina.png'
import { Button } from "@/components/ui/button"

const Navbar = () => {
  return (
    <header className="w-full fixed top-0 bg-[#F5F6F9] z-10 bg-opacity-50 backdrop-blur-xl">
      <nav className="w-full flex justify-between gap-x-20 py-6 px-12  shadow-md font-poppins text-[#2F3238] font-bold">
        <Image src={Furina} alt="furina" height={40} width={40}/>
        <div className="flex gap-x-20 items-center">
          <Link href='/' className="hover:scale-125 transition-all">
            HOME 
          </Link>
          <Link href='/about-tubes' className="hover:scale-125 transition-all">
            ABOUT
          </Link>
          <Link href='/content-based-information-retrieval' className="hover:scale-125 transition-all">
            TOOLS
          </Link>
        </div>
        <Button className="w-[100px] py-4 px-8 rounded-full">
          Login
        </Button>
      </nav>
    </header>
  )
}

export default Navbar