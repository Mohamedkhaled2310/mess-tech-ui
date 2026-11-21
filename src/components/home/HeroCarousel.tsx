'use client';

import React, { useState, useEffect } from 'react';
import Link from 'next/link';
import Image from 'next/image';
import { useLanguage } from '@/context/LanguageContext';
import { mockHeroBanners } from '@/services/mockData';
import { ChevronRight, ChevronLeft, ArrowRight, ArrowLeft } from 'lucide-react';

export default function HeroCarousel() {
  const { locale, dir } = useLanguage();
  const [current, setCurrent] = useState(0);

  // Auto slide every 5 seconds
  useEffect(() => {
    const timer = setInterval(() => {
      setCurrent((prev) => (prev + 1) % mockHeroBanners.length);
    }, 5500);
    return () => clearInterval(timer);
  }, []);

  const prevSlide = () => {
    setCurrent((prev) => (prev === 0 ? mockHeroBanners.length - 1 : prev - 1));
  };

  const nextSlide = () => {
    setCurrent((prev) => (prev + 1) % mockHeroBanners.length);
  };

  const currentBanner = mockHeroBanners[current];

  return (
    <div className="relative w-full overflow-hidden bg-slate-900 group">
      {/* Slide Image Container */}
      <div className="relative w-full h-[260px] sm:h-[340px] md:h-[420px] lg:h-[480px]">
        {mockHeroBanners.map((banner, index) => (
          <div
            key={banner.id}
            className={`absolute inset-0 transition-opacity duration-700 ease-in-out ${
              index === current ? 'opacity-100 z-10' : 'opacity-0 z-0 pointer-events-none'
            }`}
          >
            {/* Banner Image */}
            <div className="relative w-full h-full">
              <img
                src={banner.image}
                alt={banner.title[locale]}
                className="w-full h-full object-cover object-center"
              />
              {/* Soft Gradient Overlay */}
              <div className="absolute inset-0 bg-gradient-to-t from-petrol-950/70 via-transparent to-transparent md:bg-gradient-to-r md:from-petrol-950/80 md:via-petrol-900/30 md:to-transparent" />
            </div>

            {/* Slide Text Content */}
            <div className="absolute inset-0 flex items-center z-20">
              <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 w-full">
                <div className="max-w-xl text-white space-y-3 sm:space-y-4">
                  <span className="inline-block px-3 py-1 rounded-full text-xs font-bold bg-sky-500/90 text-white backdrop-blur-sm shadow-sm">
                    {banner.tag[locale]}
                  </span>

                  <h1 className="text-xl sm:text-3xl md:text-4xl font-black text-white leading-tight drop-shadow-md">
                    {banner.title[locale]}
                  </h1>

                  <p className="text-xs sm:text-sm md:text-base text-slate-200 line-clamp-2 drop-shadow">
                    {banner.subtitle[locale]}
                  </p>

                  <div className="pt-2">
                    <Link
                      href={banner.link}
                      className="inline-flex items-center gap-2 px-5 py-2.5 sm:px-6 sm:py-3 rounded-xl bg-petrol-600 hover:bg-petrol-700 text-white font-bold text-xs sm:text-sm shadow-lg hover:shadow-xl transition-all transform hover:-translate-y-0.5"
                    >
                      <span>{banner.ctaText[locale]}</span>
                      {dir === 'rtl' ? <ArrowLeft className="w-4 h-4" /> : <ArrowRight className="w-4 h-4" />}
                    </Link>
                  </div>
                </div>
              </div>
            </div>
          </div>
        ))}
      </div>

      {/* Navigation Arrows */}
      <button
        onClick={dir === 'rtl' ? nextSlide : prevSlide}
        className="absolute top-1/2 -translate-y-1/2 start-4 z-30 w-10 h-10 rounded-full bg-white/80 hover:bg-white text-petrol-900 shadow-md flex items-center justify-center transition-all opacity-0 group-hover:opacity-100"
        aria-label="Previous Slide"
      >
        <ChevronRight className="w-5 h-5" />
      </button>

      <button
        onClick={dir === 'rtl' ? prevSlide : nextSlide}
        className="absolute top-1/2 -translate-y-1/2 end-4 z-30 w-10 h-10 rounded-full bg-white/80 hover:bg-white text-petrol-900 shadow-md flex items-center justify-center transition-all opacity-0 group-hover:opacity-100"
        aria-label="Next Slide"
      >
        <ChevronLeft className="w-5 h-5" />
      </button>

      {/* Slide Indicators / Dots */}
      <div className="absolute bottom-4 left-1/2 -translate-x-1/2 z-30 flex items-center gap-2">
        {mockHeroBanners.map((_, index) => (
          <button
            key={index}
            onClick={() => setCurrent(index)}
            className={`transition-all ${
              index === current
                ? 'w-7 h-2.5 bg-sky-400 rounded-full'
                : 'w-2.5 h-2.5 bg-white/60 hover:bg-white rounded-full'
            }`}
            aria-label={`Go to slide ${index + 1}`}
          />
        ))}
      </div>
    </div>
  );
}
