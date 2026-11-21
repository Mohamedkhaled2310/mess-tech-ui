'use client';

import React, { useState } from 'react';
import Link from 'next/link';
import { useRouter } from 'next/navigation';
import { useLanguage } from '@/context/LanguageContext';
import { Phone, Lock, User, ArrowLeft, ArrowRight, ShieldCheck } from 'lucide-react';

export default function AuthLoginPage() {
  const router = useRouter();
  const { dir, t } = useLanguage();
  const [tab, setTab] = useState<'login' | 'register'>('login');

  const [phone, setPhone] = useState('');
  const [password, setPassword] = useState('');
  const [name, setName] = useState('');

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    // Simulate instant login
    localStorage.setItem('mess_user', JSON.stringify({ name: name || 'مهندس العميل', phone }));
    router.push('/account/profile');
  };

  return (
    <div className="min-h-[75vh] flex items-center justify-center px-4 py-12">
      <div className="max-w-md w-full bg-white rounded-3xl border border-slate-200 shadow-card p-6 sm:p-8 space-y-6">
        {/* Header */}
        <div className="text-center space-y-2">
          <div className="w-12 h-12 rounded-2xl bg-petrol-800 text-white font-black text-xl flex items-center justify-center mx-auto">
            M
          </div>
          <h1 className="text-2xl font-black text-petrol-900">
            {tab === 'login' ? 'تسجيل الدخول' : 'إنشاء حساب جديد'}
          </h1>
          <p className="text-xs text-slate-500">
            {tab === 'login'
              ? 'أهلاً بك مجدداً في متجر ميس تك لمعدات الشبكات'
              : 'أنشئ حسابك لمتابعة طلبياتك وحفظ عناوين الشحن والفواتير'}
          </p>
        </div>

        {/* Tab switch */}
        <div className="flex bg-slate-100 p-1 rounded-xl text-xs font-bold">
          <button
            onClick={() => setTab('login')}
            className={`flex-1 py-2 rounded-lg transition-all ${
              tab === 'login' ? 'bg-white text-petrol-900 shadow-xs' : 'text-slate-500 hover:text-slate-800'
            }`}
          >
            تسجيل الدخول
          </button>
          <button
            onClick={() => setTab('register')}
            className={`flex-1 py-2 rounded-lg transition-all ${
              tab === 'register' ? 'bg-white text-petrol-900 shadow-xs' : 'text-slate-500 hover:text-slate-800'
            }`}
          >
            حساب جديد
          </button>
        </div>

        {/* Form */}
        <form onSubmit={handleSubmit} className="space-y-4">
          {tab === 'register' && (
            <div>
              <label className="block text-xs font-bold text-slate-700 mb-1">الاسم بالكامل *</label>
              <div className="relative">
                <User className="w-4 h-4 text-slate-400 absolute top-1/2 -translate-y-1/2 start-3" />
                <input
                  type="text"
                  required
                  value={name}
                  onChange={(e) => setName(e.target.value)}
                  placeholder="محمد أحمد"
                  className="w-full ps-9 pe-4 py-2.5 text-xs rounded-xl border border-slate-200 focus:outline-none focus:ring-2 focus:ring-petrol-500"
                />
              </div>
            </div>
          )}

          <div>
            <label className="block text-xs font-bold text-slate-700 mb-1">رقم الهاتف أو البريد *</label>
            <div className="relative">
              <Phone className="w-4 h-4 text-slate-400 absolute top-1/2 -translate-y-1/2 start-3" />
              <input
                type="text"
                required
                value={phone}
                onChange={(e) => setPhone(e.target.value)}
                placeholder="010XXXXXXXX"
                className="w-full ps-9 pe-4 py-2.5 text-xs rounded-xl border border-slate-200 focus:outline-none focus:ring-2 focus:ring-petrol-500 font-mono"
              />
            </div>
          </div>

          <div>
            <div className="flex items-center justify-between mb-1">
              <label className="block text-xs font-bold text-slate-700">كلمة المرور *</label>
              {tab === 'login' && (
                <a href="#" className="text-[11px] text-sky-600 hover:underline">
                  نسيت كلمة المرور؟
                </a>
              )}
            </div>
            <div className="relative">
              <Lock className="w-4 h-4 text-slate-400 absolute top-1/2 -translate-y-1/2 start-3" />
              <input
                type="password"
                required
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                placeholder="••••••••"
                className="w-full ps-9 pe-4 py-2.5 text-xs rounded-xl border border-slate-200 focus:outline-none focus:ring-2 focus:ring-petrol-500 font-mono"
              />
            </div>
          </div>

          <button
            type="submit"
            className="w-full py-3 rounded-xl bg-petrol-700 hover:bg-petrol-800 text-white font-extrabold text-xs flex items-center justify-center gap-2 shadow-sm transition-all"
          >
            <span>{tab === 'login' ? 'دخول لحسابي' : 'إنشاء الحساب الآن'}</span>
            {dir === 'rtl' ? <ArrowLeft className="w-3.5 h-3.5" /> : <ArrowRight className="w-3.5 h-3.5" />}
          </button>
        </form>

        <div className="pt-2 text-center text-xs text-slate-400 flex items-center justify-center gap-1.5">
          <ShieldCheck className="w-3.5 h-3.5 text-emerald-600" />
          <span>بياناتك محمية ومشفرة بمعايير أمان عالية</span>
        </div>
      </div>
    </div>
  );
}
