"use client"
import Link from "next/link"

const Navbar = () => {
  return (
    <header className="w-full fixed top-0 bg-[#F5F6F9] z-10 bg-opacity-50 backdrop-blur-xl">
      <nav className="flex justify-center gap-x-20 p-6  shadow-md font-poppins text-[#2F3238] font-bold">
        <Link href='/' className="hover:scale-125 transition-all">
          HOME 
        </Link>
        <Link href='/about-tubes' className="hover:scale-125 transition-all">
          ABOUT
        </Link>
        <Link href='/content-based-information-retrieval' className="hover:scale-125 transition-all">
          TOOLS
        </Link>
        <Link href='/camera' className="hover:scale-125 transition-all">
          CAMERA
        </Link>
        <Link href='/image-scrapper' className="hover:scale-125 transition-all">
          IMG SCRAPPER
        </Link>
      </nav>
    </header>
  )
}

export default Navbar