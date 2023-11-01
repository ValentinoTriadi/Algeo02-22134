"use client"

import Cameras from './Cameras'

const Camera = () => {
  return (
    <section className="w-full flex flex-col items-center py-8 justify-center">
      <h1 className='text-2xl md:text-3xl py-4 font-semibold text-center'>Camera</h1>
      <Cameras />
    </section>
  )
}

export default Camera