"use client"

import Image from "next/image"
import Link from "next/link"

const Navbar = () => {
  return (
    <header className="w-full fixed top-0">
      <nav className="flex items-center justify-around p-5">
        <div className="min-w-[90%] h-20 bg-red-500 rounded-full flex items-center justify-center">
          <ul className="flex w-[90%] justify-evenly">
            <Link href={"/"}>
              <li className="w-auto font-mono font-black text-xl hover:text-slate-100 hover:cursor-pointer" >About Us</li>
            </Link>
            <Link href={"/CBIR"}>
              <li className="w-auto font-mono font-black text-xl hover:text-slate-100 hover:cursor-pointer" >Image</li>
            </Link>
            <Link href={"/camera"}>
              <li className="w-auto font-mono font-black text-xl hover:text-slate-100 hover:cursor-pointer" >Camera</li>
            </Link>
            {/* <Link href={"/scrap"}>
              <li className="w-auto font-mono font-black text-xl hover:text-slate-100 hover:cursor-pointer" >Scrap</li>
            </Link> */}
          </ul>
        </div>
      </nav>
    </header>
  )
}

export default Navbar